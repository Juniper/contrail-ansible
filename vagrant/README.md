## Vagrant based development environments
* Install vagrant and virtualbox (https://www.vagrantup.com/docs/installation/)
* Define your test layout
  * System use an environment variable called "layout" to read the layout from. The default for this is "vagrant\_nodes"
  *  System will look for a file "$layout".yaml in current file i.e by default, it will look for a file vagrant\_nodes.yaml
  * You can define node type, number of nodes, node size etc in that file, please refer vagrant\_nodes.yaml file included.
* Now you may manage your test environment using vagrant commands
  * vagrant up - start all VMs in your layout
  * vagrant up <node name> - start only one of the node named in the command
  * vagrant destroy - destroy all/named vms
  * vagrant --help - for the help
* Vagrant up should start the system and configure it, install docker, and start docker containers - so it should give you a
  working system in single command

I run below command to start single node all-in-one contrail system without openstack

```
# I use ansible_inventory to pass custom inventory file which should match the file name under playbooks/inventory directory
# By default it is svl_allinone_wo_os as of now

$ ansible_inventory=vagrant_registry_allinone vagrant up cc1
```