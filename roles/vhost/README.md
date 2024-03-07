# VHost

A basic role to handle vhost creation and configuration on LemonLDAP.

## Requirements

We need at Python\>=3.7 because our internal module use dataclasses.
LemonLDAP is also required, for more information about how to install
it, please check the dedicated role.

## Role Variables

``` yaml
vhost_vhosts
```

List of dictionaries representing vhost we want to configure.

## Example Playbook

Including an example of how to use your role (for instance, with
variables passed in as parameters) is always nice for users too:

    - hosts: servers
      vars:
        vhost_vhosts:
          - vhostname: demo.example.com
            exported_headers:
              - {header: x-wing, value: machin}
            access_rules:
              - {location: /accept, rule: accept}
      roles:
         - { worteks.lemonldap.vhost }

## License

MIT
