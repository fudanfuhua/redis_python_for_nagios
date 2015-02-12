#!/usr/bin/env python
import global_setting
from plugins import cpu,load,mem

def cpu_info():
	return  cpu.monitor()

def load_info():
	return load.monitor()
	

def mem_info():
	return mem.monitor()

if __name__ == "__main__":	
	cpu_info()
	load_info()
	mem_info()
