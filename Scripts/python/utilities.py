import os
import subprocess
import time
import sys
import ipaddress
import random
from urllib2 import urlopen, URLError, HTTPError
import string
import logging
import socket
import re

logger = logging.getLogger(__name__)


class Utilities(object):

    def __init__(self):
        pass

    @staticmethod
    def _cmd_async(cmd, pipe_in=None, pipe_out=False, shell=False):  # Exception not correct yet
        '''To store output and error if needed'''
        try:
            p = subprocess.Popen(
                cmd,
                shell=shell,
                stdin=pipe_in,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            if pipe_out:
                return p, None
            else:
                output, err = p.communicate()
                return output, err
        except subprocess.CalledProcessError as err:
            logger.debug(err)
            raise
        except OSError as err:
            logger.debug(err)
            logger.error("Invalid command '%s'.", cmd)
            raise Exception("'%s' command execution failed" % cmd)

    @staticmethod
    def _cmd_sync(*cmd, **kwargs):
        try:
            #print kwargs.get('pipe_in')
            if kwargs.get('pipe_in'):
                #print kwargs['pipe_in']
                # if 'pipe_in' in kwargs:
                output = subprocess.check_output(
                    cmd, stdin=kwargs['pipe_in'].stdout)
            else:
                output = subprocess.check_output(cmd)
            return output
        except subprocess.CalledProcessError as err:
            logger.debug(err)
            raise
        except OSError:
            logger.error("Invalid command '%s'.", cmd)
            raise

    @staticmethod
    def _bash_script(script, *args):
        '''This function is used for bash scripts as we want to see the output'''
        '''and for that we used check_call function from subprocess'''
        cmd = [script]
        for a in args:
            cmd.append(a)
        try:
            output = check_call(cmd)
<<<<<<< Updated upstream
        except CalledProcessError:
            print "Error: '%s' failed." % cmd
            exit('Exiting...')
        except KeyboardInterrupt:
            print "Execution aborted."
            exit('Exiting...')
        return output

    def startEndResize(self, dName):
        '''Finding out the start and end for root fs resize'''
        out = self.linuxCmd(
            "echo -e 'unit chs\nprint free' | sudo parted /dev/%s" % dName)
=======
            return output
        except subprocess.CalledProcessError:
            logger.error("Failed to execute '%s'.", cmd)
            raise
        except KeyboardInterrupt:
            logger.error("Execution aborted...")
            raise

    @staticmethod
    def _create_dir(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            logger.error("Failed to create the '%s' directory", directory)
            raise

    @staticmethod
    def _random_str(size=15, chars=None):
        if not chars:
            chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def _strip_list_items(l):
        return [x.strip() for x in l]

    @staticmethod
    def _str_to_tuple(s, delimiter=None):
        return tuple(filter(None, s.split(delimiter)))

    @classmethod
    def run_cmd(cls, cmd):
        try:
            if '|' in cmd:
                cmd = cls._strip_list_items(cmd.split('|'))
                output = None
                pipe = True
                for i in range(0, len(cmd)):
                    if i == len(cmd) - 1:
                        pipe = False
                    if output:
                        output, err = cls._cmd_async(cls._str_to_tuple(
                            cmd[i]), pipe_in=output.stdout, pipe_out=pipe)
                    else:
                        output, err = cls._cmd_async(
                            cls._str_to_tuple(cmd[i]), pipe_out=pipe)
                return output.strip(), err.strip()
            else:
                output, err = cls._cmd_async(cls._str_to_tuple(cmd))
                return output.strip(), err.strip()
        except subprocess.CalledProcessError as err:
            raise Exception("'%s' command execution failed" % (' '.join(cmd)))

    @classmethod
    def change_os_password(cls, username, password):
        try:
            cmd = "%s %s:%s | %s %s" % (
                cls.get_package_path('echo'),
                username,
                password,
                cls.get_package_path('sudo'),
                cls.get_package_path('chpasswd'))
            out, err = cls.run_cmd(cmd)
            if err:
                logger.debug(err)
                logger.warning(
                    "Unable to change the user:'%s' password", username)
                return False
            return True
        except Exception as err:
            logger.debug(err)
            raise

    @classmethod
    def list_ns(cls):
        try:
            ip = cls.get_package_path('ip')
            return cls._cmd_sync(ip, 'netns').split()
        except Exception as err:
            print err
            raise Exception("Failed to fetch the network namespaces")

    @classmethod
    def ping_host(cls, host, count=10, byte_size=56):
        try:
            logger.debug(
                "Pinging host '%s'. Count is set to '%d' and size is set to '%d'",
                host, count, byte_size)
            output = cls._cmd_sync(
                '/bin/ping', '-c', str(count), '-s', str(byte_size), host)
            logger.debug("Ping successful")
            output = output.split('\n')
            rx = re.search(r"transmitted,\s(\d+)", output[-2]).group(1)
            delay = output[-1].split('=')[1].split('/')[1]
            logger.debug(
                "Transmitted packets=%d, received packets=%s, avg rtt=%s",
                count, rx, delay)
            return True
        except subprocess.CalledProcessError as err:
            logger.warning("Host '%s'unreachable", host)
            logger.debug(err)
            return False

    @classmethod
    def get_file(cls, url, path, name=None):
        try:
            path = os.path.abspath(path)
            cls._create_dir(path)
            if not name:
                name = cls._random_str()
            path = os.path.join(path, name)
            if os.path.exists(path):
                logger.debug("'%s' file already exisits", name)
                return True
            logger.debug("Downloading file from '%s'", url)
            response = urlopen(url)
            with open(path, 'w') as f:
                f.write(response.read())
            logger.debug(
                "Download successful. Saved to '%s'", path)
            return True
        except HTTPError:
            raise
        except URLError:
            logger.error("Invalid URL '%s'", url)
            raise
        except OSError:
            raise

    @classmethod
    def get_current_directory(cls):
        # return cls._cmd_sync('pwd')
        return os.getcwd()

    @classmethod
    def get_username(cls):
        # return cls._cmd_sync('whoami')
        return socket.gethostname()

    @classmethod
    def get_package_path(cls, pkg):
        try:
            return cls._cmd_sync('which', pkg).strip()
        except Exception as err:
            logger.debug(err)
            raise Exception(
                "'%s' package doesn't exist" % pkg)

    def aliveHosts(self, subnet):
        '''To find alive hosts, you are gonna need nmap tool installed'''
        out = cls.run_cmd("sudo nmap -sn %s" % subnet)

    def startEndResize(self, dName):
        '''Finding out the start and end for root fs resize'''
        out = cls.run_cmd("echo -e 'unit chs\nprint free' | sudo parted /dev/%s" % dName)
>>>>>>> Stashed changes
        t1 = "Disk /dev/%s: " % dName
        t2 = "2      "
        i1 = out.find(t1)
        i2 = out.find(t2)
        end = out[i1 + len(t1):i1 + len(t1) + out[i1 + len(t1):].find("\n")]
        start = out[i2 + len(t2):i2 + len(t2) + out[i2 + len(t2):].find(" ")]
        return start, end

    def randIPs(self, subnet, count=-1, rangeStart=0, rangeEnd=-1):
        '''Output <count> random IPs from the <subnet>'''
        '''range: its value is in the form start-end'''
        ipAddr = {'IP Addresses': []}
        net = list(ipaddress.ip_network(unicode(subnet)).hosts())[
            rangeStart:rangeEnd]
        while True:
            addr = random.choice(net)
            if str(addr) not in ipAddr['IP Addresses']:
                ipAddr['IP Addresses'].append(str(addr))
            if len(
                    ipAddr['IP Addresses']) == count or len(
                    ipAddr['IP Addresses']) == len(net):
                break
        return ipAddr
