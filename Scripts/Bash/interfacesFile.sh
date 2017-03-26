#!/bin/bash
cat << EOF > interfaces 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
# The loopback network interface
auto lo
iface lo inet loopback

#Your static network configuration
auto $1
iface $1 inet static
address $2
netmask $3
gateway $4
dns-nameservers $5 $6

EOF

exit 0
