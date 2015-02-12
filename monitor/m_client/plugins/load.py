#!/usr/bin/env python 
import commands
 
def monitor():
     shell_command = 'uptime'
     status,result = commands.getstatusoutput(shell_command)
     if status != 0:
         value_dic = {'status':status}
     else:
         uptime = result.split(',')[:1][0]
         load1,load5,load15 = result.split('load average:')[1].split(',')
         #print result.split('load average:')
         value_dic = {
                                    'status': status,
                                    'uptime': uptime,
                                    'load1': load1,
                                    'load5': load5,
                                    'load15': load15,
                                    'status': status,
                                    }
     return value_dic   
if __name__ == '__main__':
     print monitor()
        