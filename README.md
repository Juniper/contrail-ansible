# Contrail-ansible
Ansible code to provision contrail system

Currently we follow an all-in-one repo for all playbooks and contrail specific roles.

Also we are taking a different approach than standard single tiny reusable roles approach, to have a hierarchical
roles and subroles approach to have a composable hierarchical role[s], so that I can have all code in same repo but
keeping logical separation with subroles and tags to make the code composable.

If things go unmanageable in future, we could go towards splitting roles.

NOTE: Current code only tested with single node setup, there are little bit more work needed to support to have multi-node setup.

# Quickstart
Here are the step by step instructions to quickly setup contrail containers.

https://github.com/Juniper/contrail-ansible/wiki/Quickstart-Guide-with-ini-file-based-inventory

https://github.com/Juniper/contrail-ansible/wiki/Quickstart-guide-with-directory-based-inventory

## Running contrail containers using contrail-ansible
Part of the code in contrail-ansible is supposed to create a native ansible interface to setup base system and orchestrate
/provision contrail containers on top of them, if people don't want to use more featured orchestration/provisioning
systems like server manager. This functionality is supposed to provide a basic ansible native interface and will only
handle operating system setup on base nodes and run/orchestrate containers on top of them. This section brief about the
process to run contrail containers using contrail-ansible.

* Install ansible version >= 2.0 - please refer http://docs.ansible.com/ansible/intro_installation.html
* Get contrail-ansible code - you may get from github repository or any other packaged versions.
* Install any dependent roles - this step will eventually go away once we moved all dependent roles inside contrail-ansible

    ```
    $ cd contrail-ansible
    $ ansible-galaxy install -r requirements.yml
    ```

* Create an inventory file - please refer the [sample inventory file provided](playbooks/inventory/examples/single-controller-multi-compute-svl)
   to create one for you. For a standard single controller, multi-compute setup, it would only need to add/change the IP
   addresses. You may also have to refer ansible code and variable defaults for more advanced configurations

    * Set variable contrail_docker_registry to valid registry server address in case of using docker registry to distribute
     docker container images

       ```
     
       contrail_docker_registry=10.84.34.155:5000
       contrail_docker_registry_insecure=True
    
       ```

    * Copy container image tar files to contrail-ansible/playbooks/container_images/ and make sure contrail_docker_registry
    is NOT set in the inventory, in case of NOT using docker registry to distribute the images and to have ansible to
    distribute and load docker images.

      ```
      $ ls ~/contrail-ansible/playbooks/container_images/
        contrail-agent-3.2.0.0-3004.tar.gz      contrail-analyticsdb-3.2.0.0-3004.tar.gz  contrail-lb-3.2.0.0-3004.tar.gz
        contrail-analytics-3.2.0.0-3004.tar.gz  contrail-controller-3.2.0.0-3004.tar.gz   vrouter-module-compiler-redhat7-3.2.0.0-3004.tar.gz
    
      ```
* Copy and edit contrailctl config files - there are per container config files i.e controller.conf for controller,
    analytics.conf for analytics, analyticsdb.conf for analyticsdb, lb.conf for lb. Ansible playbook expect those config
    files are configured separately and present in three possible locations within the ansible node filesystem -
    playbooks/files/contrailctl/, playbooks/contrailctl/, /etc/contrailctl/. Please refer example configuration files
    kept under [contrail-docker](https://github.com/Juniper/contrail-docker/tree/master/tools/python-contrailctl/examples/configs)
    for more details.
* Run ansible-playbook with site.yml pointing to your own inventory file

    ```
    $ cd playbooks
    $ ansible-playbook -i inventory/examples/single-controller-multi-compute-svl site.yml
    ```

Now contrail-controller node should have all contrail-controller specific containers running and all computes have agent
container running. 

Note that containers will take few minutes to come up completely, once they are up, you will be able to connect to webui
using static auth and will be able to see the system status and would be able to do various operations.

Note: 
* This code support only single controller node at this moment, but you can have multiple compute nodes.
* Currently no openstack setup is supported, only contrail components setup supported.
* Default configuration (without openstack) use webui static auth since there is no authentication service. So users
have to use static auth credentials to connect to webui.
