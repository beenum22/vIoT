#!/bin/bash

source /home/$USER/devstack/openrc admin admin
echo "openrc sourced for admin credentials."
echo "+------------------------------------+"
nova flavor-create mm.micro m1 256 1 1
nova flavor-create mm.nano m2 128 1 1
nova flavor-create mm.pico m3 100 1 1
nova flavor-create mm.femto m4 64 1 1
nova flavor-create mm.atto m5 32 1 1
nova flavor-create mm.zepto m6 16 1 1
echo "New flavors added to Nova."
echo "+------------------------------------+"

glance image-create --name="trusty-amd64" --container-format=bare --disk-format=raw --visibility=public < /home/$USER/vIoT/Images/trusty-server-cloudimg-amd64-root.tar.gz
glance image-create --name="trusty-armhf" --container-format=bare --disk-format=raw --visibility=public < /home/$USER/vIoT/Images/trusty-server-cloudimg-armhf-root.tar.gz
#glance image-create --name="cirros-armhf" --container-format=bare --disk-format=raw --visibility=public < /home/$USER/vIoT/Images/cirros-0.3.4-arm-rootfs.img.gz
#glance image-create --name="cirros_x86_64" --container-format=bare --disk-format=raw --visibility=public < /home/$USER/vIoT/Images/cirros-0.3.4-x86_64-rootfs.img.gz
echo "Added x86_64 and ARM images to Glance."
echo "+------------------------------------+"
