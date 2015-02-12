#!/usr/bin/env python 
import commands
import m_handle
import time
import global_setting

value = None
while  value == None:
    value = str(m_handle.fetch_monitor_lists()) 
    print "\033[32;1m>>>>>>>>>>>>>>>>>>>>>    %s \033[0m"  %  value
    str_value  =str(value)
    time.sleep(1)
        #save data to save_data file
f = open("save_data" , "w")
f.write(str_value)
f.close()
print "\033[35;1m     save_data file have data    \033[0m"
        #get data from save_data then mail manager
shell = "cat save_data"
command_status, command_result = commands.getstatusoutput(shell)
if command_status == 0:
    if command_result is not None:
        shell_command = "mail -s 'Hello , that is ok' koko@koko-Lenovo-IdeaPad-Y480 -- -f koko@example.com < save_data"
        status , result = commands.getstatusoutput(shell_command)
        if status == 0:
            print "\033[33;1m>>>>>>>>>>>>>>>>>>>>>>OK, mail had send to manager  !!!!!!<<<<<<<<<<<<<<<<<<<<<<\033[0m"
        
        

    