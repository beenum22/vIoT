#!/bin/bash

source $1/devstack/openrc admin admin
echo "openrc sourced for admin credentials."

echo "Adding new flavors to the Nova."
nova flavor-create m2.micro 6 256 1 1
nova flavor-create m2.nano 7 128 1 1
nova flavor-create m2.pico 8 100 1 1
nova flavor-create m2.femto 9 64 1 1

echo "Adding armhf images to the Glance."
#glance image-create --name="trusty-amd64" --container-format=bare --disk-format=raw --visibility=public < /home/ubuntu/backup_old_ubuntu/trusty-server-cloudimg-amd64-root.tar.gz
glance image-create --name="trusty-armhf" --container-format=bare --disk-format=raw --visibility=public < $1/Images/trusty-server-cloudimg-armhf-root.tar.gz
#glance image-create --name="cirros" --container-format=bare --disk-format=raw --visibility=public < /home/iotubuntu/images/cirros-0.3.4-arm-rootfs.img.gz
#glance image-create --name="cirros_x86_64" --container-format=bare --disk-format=raw --visibility=public < /home/iotubuntu/images/cirros-0.3.4-x86_64-rootfs.img.gz
