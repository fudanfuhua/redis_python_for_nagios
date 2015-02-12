#!/usr/bin/env python 
import commands

def monitor():
    shell_command = " free -m | awk '{ print $3 }' | tail -3 | tr -t '\n' '  ' "
    status,result = commands.getstatusoutput(shell_command)
    if status != 0: 
        value_dic = {'status': status }
    else:
        mem, cache, swap = result.split()
        value_dic = {
                     'status': status,
                     'swap': swap,
                     'mem':mem,
                     }
    return value_dic
if __name__ == "__main__":
    print monitor()
