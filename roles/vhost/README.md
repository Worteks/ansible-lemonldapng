# VHost

A basic role to handle vhost creation and configuration on LemonLDAP.
Currently we only handle vhosts creation on nginx, the idea behind that
role is also to create a generic way to configure vhosts on nginx side
and LemonLDAP manager (that part is not yet implemented).

## Role Variables

``` yaml
vhost_vhosts
```

List of dictionaries representing vhost we want to configure.

## Example Playbook

    - hosts: servers
      vars:
        vhost_vhosts:
          - vhostname: demo.example.com
            configure_default_location: true
            https: true
            port: 443
            redirect_http_to_https: true
            http_proxy_backend: http://mybackend.example.com
      roles:
         - { worteks.lemonldap.vhost }

## License

MIT
