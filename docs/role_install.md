Role install from LemonLDAP::NG collection
==========================================

This is the install role of the LemonLDAP::NG collection. It can be used to install
and do some basic configuration of LemonLDAP::NG.

Requirements
------------

Pulling packages from the LLNG repository, which is done through the `install`
role.

Roles Variables
--------------
Currently we provide those roles :
 - [Install](docs/role_install.md)

 * `lemonldap_do_soap`, toggles SOAP-related webserver configuration, defaults to `False`.
 * `lemonldap_domain`, the root domain of your LLNG setup, defaults to `changeme.com`.
 * `lemonldap_webserver`, the webserver running LLNG, defaults to `nginx`, could be changed to `apache`.

Dependencies
------------

None

Example Playbook
----------------

```
    - hosts: servers
      vars:
        lemonldap_domain: my.org
        lemonldap_webserver: nginx
      roles:
         - { role: worteks.lemonldap.install, lemonldap_domain: my.org, lemonldap_webserver: nginx }
```

License
-------

MIT

Author Information
------------------

See [AUTHORS](AUTHORS)
