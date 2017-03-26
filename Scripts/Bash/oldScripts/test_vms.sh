#!/bin/bash

source /home/$USER/devstack/openrc  admin demo

nova boot --image trusty-amd64 --flavor m2.micro test1
echo "test VM launched"
echo "add floating ip"

nova floating-ip-create
nova add-floating-ip test1 
