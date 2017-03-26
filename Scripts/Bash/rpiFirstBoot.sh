#!/bin/bash
echo "Initializing Pi and installing necessary packages"
sudo apt-get -y install git python python-pip
pip install netifaces
pip install ipaddress
sudo apt-get update -y
sudo apt-get upgrade -y
sudo add-apt-repository ppa:ubuntu-lxc/lxd-git-master
sudo apt-get update
sudo apt-get -y install lxd lxd-client

sudo lxd init
lxc profile set default raw.lxc lxc.aa_allow_incomplete=1

rm $0