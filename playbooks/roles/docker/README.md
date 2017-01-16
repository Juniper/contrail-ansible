docker
======

A role that installs Docker via https://get.docker.io

Requirements
------------

Role Variables
--------------

A list of insecure registries to authorize within the walled garden
```
docker_insecure_registries:
  - registry.mydomain

Dependencies
------------
andrewrothstein.curl - we use curl rather than the ansible get_url module due to issues with ubuntu_trusty's version version of python (v2.7.6) [SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) in TLS/SSL correctly with get.docker.io


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: andrewrothstein.docker, insecure_registries : ["localhost:5000"], docker_mirror : "https://myinstaller.endpoint.io" }

License
-------

MIT

Author Information
------------------

Andrew Rothstein andrew.rothstein@gmail.com
