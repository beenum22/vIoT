#!/Users/muneebahmad/anaconda/bin/python

import ipaddress
from utilities import Utilities
import random

u = Utilities()
l = u.randIPs('192.168.1.0/24', 10)
print l 
'''
try:
    i = raw_input('Enter value:')
    net = ipaddress.ip_network(unicode(i))
    print type(net[0])
    #print random.choice(net)

    #for addr in net:
    	#print str(addr)
except NameError:
    print "Error: Incorrect value."
'''