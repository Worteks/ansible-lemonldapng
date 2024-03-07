from ansible.module_utils.basic import AnsibleModule
from ansible_collections.worteks.lemonldap.plugins.module_utils.utils import (
    VirtualHost, get_llng_binary_path)


def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            vhostname=dict(required=True, type=str),
            access_rules=dict(required=False, type="list", default=[], elements="dict"),
            exported_headers=dict(
                required=False, type="list", default=[], elements="dict"
            ),
            force=dict(required=False, type="bool", default=False),
            https=dict(required=False, type="bool", default=False),
            maintenance=dict(required=False, type="bool", default=False),
        ),
        supports_check_mode=False,
    )
    result = dict(changed=False, original_message="", message="")
    llng_bin = get_llng_binary_path()
    if module.check_mode or llng_bin is None:
        module.exit_json(**result)

    base_cmd = [str(llng_bin)] + (["-yes", "1"] if module.params["force"] else [])
    cmd = []
    vhost = VirtualHost(
        name=module.params["vhostname"],
        exported_headers=module.params["exported_headers"],
        access_rules=module.params["access_rules"],
        https=module.params["https"],
    )
    cmd += (
        vhost.generate_exported_headers_cmd_part()
        + vhost.generate_access_rules_cmd_part()
        + vhost.generate_https_cmd_part()
        + vhost.generate_maintenance_cmd_part()
    )
    rc, stdout, stderr = module.run_command(
        args=base_cmd + ["addKey"] + cmd,
        check_rc=True,
    )
    result["message"] = stdout
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
