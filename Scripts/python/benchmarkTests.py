#!/usr/bin/python

import os
from subprocess import *
import time
import sys
from threading import Thread


class novaTime(object):

    def __init__(self, options):
        self.options = options

    def startTest(self):
        t = Thread(target=self.novaBoot)
        t.start()
        self.time()

    def run_cmd(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

    def novaBoot(self):
        self.run_cmd("source /home/$USER/devstack/openrc admin admin")
        cmd = "openstack server create --image %s --flavor %s --max %s %s" % (
            self.options.image, self.options.flavor, str(self.options.containerCount), self.options.name)
        self.run_cmd(cmd)
        '''
        for i in range (self.options.containerCount):
            novaB = "nova boot --image %s --flavor %s %s%s" % (self.options.image, self.options.flavor, self.options.name, i)
            self.run_cmd(novaB)
            return None
        '''

    def time(self):
        startTime = time.time()
        while True:
            t1 = time.time()
            try:
                assert (int(self.run_cmd("nova list | grep -co 'ERROR'")) == 0)
            except AssertionError:
                print "Instance/s went into error state"
                break
            finally:
                runCont = int(self.run_cmd("nova list | grep -co 'ACTIVE'"))
                buildCont = int(self.run_cmd("nova list | grep -co 'BUILD'"))
                print "Running containers: %s" % runCont
                print "Building containers: %s" % buildCont
            t2 = time.time()
            novaListTime = t2 - t1
            if runCont == self.options.containerCount:
                print "Successfully started desired number of containers"
                totalTime = time.time() - startTime - novaListTime
                print "Deleting containers..."
                for j in range(1, self.options.containerCount + 1):
                    self.run_cmd("nova delete test-%s" % j)
                print "Successfully deleted"
                print "----------------------\n"
                print "Total time : %s sec\n" % totalTime
                print "----------------------\n"
                with open("times.txt", "a") as myfile:
                    myfile.write("%s  :  %s  :  %s" % (self.options.containerCount, totalTime, self.options.image))
                break
            '''
            else:
                currentTime = time.time() - startTime - novaListTime
                print "'nova list' execution time is %s " % currentTime
            '''
