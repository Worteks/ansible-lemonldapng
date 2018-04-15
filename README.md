Ansible LemonLDAP::NG role
=========

This is the ansible LemonLDAP::NG role. It can be used to install LemonLDAP::NG on a server.

Requirements
------------

Pulling packages from the LLNG repository, which is to be installed by this role.

Role Variables
--------------

 * `lemonldap_do_soap`, toggles SOAP-related webserver configuration, defaults to `False`.
 * `lemonldap_domain`, the root domain of your LLNG setup, defaults to `changeme.com`.
 * `lemonldap_webserver`, the webserver running LLNG, defaults to `apache`, could be changed to `nginx`.

Dependencies
------------

None

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: lemonldapng, lemonldap_domain: my.org lemonldap_webserver: nginx }
```

License
-------

MIT

Author Information
------------------

 * Thibaut Demaret
 * Raphaël Hoareau
 * Eric Marques
 * Clément Oudot
 * Samuel Martin Moro
 * Paul Curie
