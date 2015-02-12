#!/usr/bin/env python
import commands




shell = "cat save_data"
command_status, command_result = commands.getstatusoutput(shell)
if command_status == 0:
	if command_result is not None:
        	shell_command = "cat save_data > mail -s 'that is ok' koko@koko-Lenovo-IdeaPad-Y480  -- -f koko@qq.com"
		status,result = commands.getstatusoutput(shell_command)
	        print status
		if status == 0:
			print "\033[33;1m>>>>>>>>>>>>OK, we have a success!!!!!!<<<<<<<<<<<<<<<<<<\033[0m"
        
