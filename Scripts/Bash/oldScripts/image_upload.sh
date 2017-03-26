#!/bin/bash
source /home/ubuntu/devstack/openrc admin admin


glance image-create --name="trusty-amd64" --container-format=bare --disk-format=raw --visibility=public < /home/ubuntu/backup_old_ubuntu/trusty-server-cloudimg-amd64-root.tar.gz
#glance image-create --name="trusty-armhf" --container-format=bare --disk-format=raw --visibility=public < /home/iotubuntu/images/trusty-server-cloudimg-armhf-root.tar.gz
#glance image-create --name="cirros" --container-format=bare --disk-format=raw --visibility=public < /home/iotubuntu/images/cirros-0.3.4-arm-rootfs.img.gz
#glance image-create --name="cirros_x86_64" --container-format=bare --disk-format=raw --visibility=public < /home/iotubuntu/images/cirros-0.3.4-x86_64-rootfs.img.gz
echo "images uploaded"
