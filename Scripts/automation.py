#!/usr/bin/python

import os
import ConfigParser
from optparse import OptionParser
import time
import sys
from python.tasks import Tasks
from python.utilities import Utilities


class runTest(object):

    def __init__(self, argv):
        usage = ('python %prog <add variables here>')
        parser = OptionParser(
            description='Main code for Automation. You need to mention the task argument!',
            version="0.1",
            usage=usage)
        config = ConfigParser.ConfigParser()
        config.read('config.ini')

        parser.add_option(
            "--workDir",
            "-w",
            dest='workDir',
            default=config.get("DEFAULT", "workDir"),
            type='str',
            help="Working Directory")
        '''
        parser.add_option(
            "--armCC",
            "-c",
            dest='armCC',
            default=config.get("DEFAULT", "armCC"),
            type='str',
            help="ARM Cross Compile path.")
        '''
        parser.add_option(
            "--stackDir",
            dest='stackDir',
            default=config.get("DEFAULT", "stackDir"),
            type='str',
            help="stack directory path.")
        parser.add_option(
            "--pubSubnet",
            "-n",
            dest='pubSubnet',
            default=config.get("DEFAULT", "pubSubnet"),
            type='str',
            help="Public subnet.")
        parser.add_option(
            "--pubGw",
            "-g",
            dest='pubGw',
            default=config.get("DEFAULT", "pubGw"),
            type='str',
            help="Public Gateway.")
        parser.add_option(
            "--controllerIp",
            "-i",
            dest='controllerIp',
            default=config.get("DEFAULT", "controllerIp"),
            type='str',
            help="Controller ip.")
        parser.add_option(
            "--task",
            "-t",
            dest='task',
            default='muneeb',
            type='str',
            help="Enter controller/compute/rpiExt to start corresponding task.")
        parser.add_option(
            "--source",
            dest='source',
            default=config.get("DEFAULT", "source"),
            type='str',
            help="Enter the source for OpenStack packages.")
        (options, args) = parser.parse_args()
        print "-----------"
        # print options.task
        if options.task == 'controller':
            parser.add_option(
                "--floatRange",
                "-x",
                dest='floatRange',
                default=config.get("CONTROLLER", "floatRange"),
                type='str',
                help="Float/Public IP range available for VMs.")
            parser.add_option(
                "--flatInt",
                "-f",
                dest='flatInt',
                default=config.get("CONTROLLER", "flatInt"),
                type='str',
                help="Flat interface for controller host")
            parser.add_option(
                "--pubInt",
                "-p",
                dest='pubInt',
                default=config.get("CONTROLLER", "pubInt"),
                type='str',
                help="Public interface for controller host.")
            parser.add_option(
                "--repos",
                "-r",
                dest='repos',
                default=config.get("CONTROLLER", "repos"),
                type='str',
                help="List of repos needed for controller.")
        elif options.task == 'rpiExt' or options.task == 'compute':
            parser.add_option(
                "--repos",
                "-r",
                dest='repos',
                default=config.get("RPI", "repos"),
                type='str',
                help="List of repos needed for compute.")
            parser.add_option(
                "--dName",
                "-d",
                dest='dName',
                default=config.get("RPI", "dName"),
                type='str',
                help="Device Name.")
            parser.add_option(
                "--os",
                "-o",
                dest='os',
                default=config.get("RPI", "os"),
                type='str',
                help="Operating system to install.")
            parser.add_option(
                "--imageStatus",
                "-s",
                dest='imageStatus',
                default=config.get("RPI", "imageStatus"),
                type='str',
                help="Check if sdCard image is ready or not.")
        (options, args) = parser.parse_args()
        #test = Tasks(options)
        # test.rpiConfig()
        if ((len(args) != 0)):
            parser.print_help()
            sys.exit(1)
        # print options
        task = Tasks(options)
        if options.task == 'rpiExt':
            print options
            # task.rpiConfig()
        elif options.task == 'controller':
            print options
            task.controllerSetup()
        elif options.task == 'compute':
            print options
            task.computeSetup()
        else:
            parser.error("Unknown Task named '%s'." % options.task)

if __name__ == "__main__":
    runTest(sys.argv)
