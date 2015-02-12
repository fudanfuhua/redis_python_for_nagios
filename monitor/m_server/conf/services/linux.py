#!  /usr/bin/env python
from generic import DefaultService
class cpu(DefaultService):
    def __init__(self):
        self.name = "cpu"
        self.interval = 10
        self.plugin_name = 'cpu_info'
        self.triggers = { 
                    'iowait':  [ 'persentage',5.5,90],
                    'system': [ 'persentage', 5 , 20],
                    'idle': [ 'persentage', 92,90],
                    'user': [ 'persentage',80,90],
                    'steal': [ 'persentage',80,90],
                    'nice': [ 'persentage', 80, 90],
                    }
        self.temp_data = { 
                    'iowait':  {'time':0, 'status_data': [ ] },
                    'system': {'time':0, 'status_data': [ ] },
                    'idle': {'time':0, 'status_data': [ ] },
                    'user': {'time':0, 'status_data': [ ] },
                    'steal': {'time':0, 'status_data': [ ] },
                    'nice': {'time':0, 'status_data': [ ] },
                    }
        
        self.It_operator = ['idle' ,]  
    

class memory(DefaultService):
    def __init__(self):
        self.name = 'memory'
        self.plugin_name = 'mem_info'
        #interval come from gennetic  default    interval = 300
        self.triggers = {
                    'mem': ['int', 3700,3800],
                    'swap': ['int',4500,4700],
                    }
        
        self.temp_data = {
                    'mem': {'time':0, 'status_data': [ ] },
                    'swap': {'time':0, 'status_data': [ ] },
                    }

class load(DefaultService):
    def __init__(self):
        self.name = 'load'
        self.plugin_name = 'load_info'
        self.Interval = 12
        self.triggers = {
                    'load1': [ int, 4 ,9],
                    'load5': [ int, 3,7],
                    'load15': [ int, 3, 9],
                    }
        # you must change self.tmp_data keys if your update self.triggers keys, self.tmp_data is used to excute critical.
        self.temp_data = {
                    'load1': {'time':0, 'status_data': [ ] },
                    'load5': {'time':0, 'status_data': [ ] },
                    'load15': {'time':0, 'status_data': [ ] },
                    }
    