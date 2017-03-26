#!/bin/bash

sudo ovs-vsctl show
sudo ovs-vsctl add-port br-ex ens38

echo "Interface added"
