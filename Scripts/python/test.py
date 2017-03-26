from subprocess import *

def linuxCmd(cmd):
        '''To store output and error if needed'''
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def bashScript(script, *args):
    '''This function is used for bash scripts as we want to see the output and for that we used check_call function from subprocess'''
    cmd = [script]
    for a in args:
        cmd.append(a)
    output = check_call(cmd)
    return output