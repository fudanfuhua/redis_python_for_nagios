#! /usr/bin/env python 
import commands

def monitor():
    shell_command = 'sar 1 3 | sed -n  "7p"'
    status, result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status': status}
    else:
        user,nice,system,iowait,steal,idle = result.split()[2:]
        value_dic = {
                     'status': status,
                     'user': user,
                     'nice': nice,
                     'system': system,
                     'iowait': iowait,
                     'steal': steal,
                     'idle': idle,
                     }
    return value_dic

if  __name__ == "__main__":
    print monitor()
