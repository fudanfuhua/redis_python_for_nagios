import templates
import copy


#for user hehe########################################################
h1  = templates.LinuxGeneraiServices()
h1.hostname = 'hehe_server'
h1.ip_address = '127.0.0.1'
h1.port = 22
h1.os = 'ubuntu'
h1.services['cpu'].triggers['iowait'][1] = 30

#print  "change h1.cpu.trigger:" ,h1.services['cpu'].triggers['iowait'][1]
#print "h1 memory: "  , h1.services['memory'].interval
#for use xixi############################################################
h2 = templates.LinuxGeneraiServices()
h2.hostname = 'xixi_server'
h2.ip_address = '192.168.1.104'
h2.port = 22
h2.os = 'Centos'
h2.services['cpu'].interval = 11
del h2.services['memory']

#print  "change h2.cpu.trigger:" ,h2.services['cpu'].triggers['iowait'][1]
#print "h2 delete memory"
#######################    lists        #######################################
monitor_lists = [h1,h2]


