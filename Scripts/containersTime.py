#!/usr/bin/python

import os
from optparse import OptionParser
from subprocess import *
import time
import sys
from python.benchmarkTests import novaTime


class runTest(object):

    def __init__(self, argv):
        usage = ('python %prog <add variables here>')
        parser = OptionParser(
            description='Main code to record excecution times',
            version="0.1",
            usage=usage)
        parser.add_option(
            "--containers",
            "-c",
            dest='containerCount',
            default='1',
            type='int')
        parser.add_option(
            "--image",
            "-i",
            dest='image',
            default='cirros-lxd',
            type='str')
        parser.add_option(
            "--flavor",
            "-f",
            dest='flavor',
            default='m2.femto',
            type='str')
        parser.add_option(
            "--name",
            "-n",
            dest='name',
            default='test',
            type='str')
        (options, args) = parser.parse_args()
        if ((len(args) != 0)):
            parser.print_help()
            sys.exit(1)
        # print options
        exec_time = novaTime(options)
        exec_time.startTest()
if __name__ == "__main__":
    runTest(sys.argv)
