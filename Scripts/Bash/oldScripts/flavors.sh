#!/bin/bash

source /home/iotubuntu/devstack/openrc admin admin
nova flavor-create m2.micro 6 256 1 1
nova flavor-create m2.nano 7 128 1 1
nova flavor-create m2.pico 8 100 1 1
nova flavor-create m2.femto 9 64 1 1

nova flavor-list
echo "flavors added"
