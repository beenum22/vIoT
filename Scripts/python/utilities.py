#!/usr/bin/python

import os
from subprocess import *
import time
import sys
from threading import Thread
import ipaddress
import random


class Utilities(object):

    def __init__(self):
        #self.options = options
        pass

    def aliveHosts(self, subnet):
        '''To find alive hosts, you are gonna need nmap tool installed'''
        out = linuxCmd("sudo nmap -sn %s" % subnet)

    def linuxCmd(self, cmd):
        '''To store output and error if needed'''
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

    def bashScript(self, script, *args):
        '''This function is used for bash scripts as we want to see the output and for that we used check_call function from subprocess'''
        cmd = [script]
        for a in args:
            cmd.append(a)
        output = check_call(cmd)
        return output

    def startEndResize(self, dName):
        '''Finding out the start and end for root fs resize'''
        out = self.linuxCmd("echo -e 'unit chs\nprint free' | sudo parted /dev/%s" % dName)
        t1 = "Disk /dev/%s: " % dName
        t2 = "2      "
        i1 = out.find(t1)
        i2 = out.find(t2)
        end = out[i1 + len(t1):i1 + len(t1) + out[i1 + len(t1):].find("\n")]
        start = out[i2 + len(t2):i2 + len(t2) + out[i2 + len(t2):].find(" ")]
        return start, end

    def sshPassLess(self, hostname, ip):
        '''To ssh into host with a public key'''
        pass

    def randIPs(self, subnet, count=-1, rangeStart=0, rangeEnd=-1):
        '''Output <count> random IPs from the <subnet>'''
        '''range: its value is in the form start-end'''
        ipAddr = {'IP Addresses':[]}
        net = list(ipaddress.ip_network(unicode(subnet)).hosts())[rangeStart:rangeEnd]
        while True:
            addr = random.choice(net)
            if str(addr) not in ipAddr['IP Addresses']:
                ipAddr['IP Addresses'].append(str(addr))
            if len(ipAddr['IP Addresses']) == count  or len(ipAddr['IP Addresses']) == len(net):
                break
        return ipAddr

    def test(self):
        o = "Hi"
        return o
