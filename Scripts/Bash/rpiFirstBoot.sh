#!/bin/bash
echo "Installing Git, Python and neccessary packages"
apt-get -y install git python python-pip
pip install netifaces
pip install ipaddress
echo "Installation successful."
echo "Upgrading OS"
apt-get update -y
apt-get upgrade -y
echo "Upgrade successful"
# ADD INTERFACE CHANGE PART HERE
echo "Interface naming changed to classical format"
echo "Installing LXD and it's client"
apt-get -y install lxd=2.8-0ubuntu1~ubuntu16.04.1 lxd-client=2.8-0ubuntu1~ubuntu16.04.1
echo "Install successful"
echo "Initializing LXD..."
lxd init
echo "Setting turning off APPARMOR for LXD default profile due to some issues"
lxc profile set default raw.lxc lxc.aa_allow_incomplete=1
echo "Adding Swap..."
./addSwap.sh $1
echo "Swap added successfully"

rm $0