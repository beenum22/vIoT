#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import sys
import netifaces
from utilities import Utilities


class Tasks(Utilities):
    """Automation scripts for vIoT setup"""

    def __init__(self, options):
        super(Tasks, self).__init__()
        self.options = options  # dName, size, OS
        self.util = Utilities()

    def rpiConfig(self):
        '''RPi Configuration'''
        #  Installing OS
        print "+----------------------------------+"
<<<<<<< Updated upstream
        self.linuxCmd("xzcat /home/$USER/vIoT/Images/%s -v | sudo dd of=/dev/%s bs=32M status=progress" %
                      (self.options.os, self.options.dName))
=======
        self.run_cmd("xzcat /home/$USER/vIoT/Images/%s -v | sudo dd of=/dev/%s bs=32M status=progress" % (self.options.os, self.options.dName))
>>>>>>> Stashed changes
        print "'%s' successfully installed to '/dev/%s" % (self.options.os, self.options.dName)
        print "+----------------------------------+"
        #  Getting start and end value needed for resizing.
        start, end = self.startEndResize(self.options.dName)
        # print "Installing OS '%s' and resizing it's Filesystem." %
        self._bash_script(
            'Bash/rpiConfigExt.sh',
            self.options.dName,
            start,
            end)
        print "+----------------------------------+"
        print "Setup Successful."
        print "+----------------------------------+"
        print "Remove the microSDcard now."
        print "+----------------------------------+"
        # return out

    def controllerSetup(self):
        '''Setting up OpenStack Controller'''
        print "+----------------------------------+"
        print "OpenStack Controller setup started..."
        print "+----------------------------------+"
        if self.options.pubInt == 'no':
            #  For private use only
            print "Private mode selected."
<<<<<<< Updated upstream
            self.bashScript('Bash/localconf.sh', self.options.task,
                            self.options.controllerIp, self.options.flatInt)
=======
            self._bash_script('Bash/localconf.sh', self.options.task, self.options.controllerIp, self.options.flatInt)
>>>>>>> Stashed changes
        else:
            #  For public use only
            print "Public mode selected."
            self._bash_script(
                'Bash/localconf.sh',
                self.options.task,
                self.options.controllerIp,
                self.options.flatInt,
                self.options.pubInt,
                self.options.pubSubnet,
                self.options.pubGw,
                self.options.floatRange)
        print "+----------------------------------+"
        print "local.conf generated."
        print "+----------------------------------+"
<<<<<<< Updated upstream
        if self.options.source == 'custom':
            print "Custom location selected for OpenStack packages"
            self.bashScript('Bash/controllerSetup.sh', self.options.repos, self.options.source)
        else:
            print "Default location selected for OpenStack packages"
            self.bashScript('Bash/controllerSetup.sh', self.options.repos, self.options.source)
=======
        self._bash_script('Bash/controllerSetup.sh', self.options.repos)
>>>>>>> Stashed changes
        print "Setup Successful."
        print "Go nuts!"
        print "+----------------------------------+"

    def computeSetup(self):
        '''Setting up OpenStack Compute Nodes'''
        #  Find host IP
        netifaces.ifaddresses('eth0')
        hostIp = netifaces.ifaddresses('eth0')[2][0]['addr']
        print "+----------------------------------+"
        print "Host IP is %s" % hostIp
        print "+----------------------------------+"
<<<<<<< Updated upstream
        self.bashScript('Bash/localconf.sh', self.options.task,
                        hostIp, self.options.controllerIp)
=======
        self._bash_script('Bash/localconf.sh', self.options.task, hostIp, self.options.controllerIp)
>>>>>>> Stashed changes
        print "+----------------------------------+"
        print "local.conf generated."
        print "+----------------------------------+"
        print self.options.repos
        self._bash_script('Bash/rpiConfigInt.sh', self.options.repos)
        print "Setup Successful."
