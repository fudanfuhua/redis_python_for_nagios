#!/usr/bin/env python 
import threading
import time
import global_setting
import plugin_api
import redis_connecter as redis
import json
import sys
import pickle
hostname = 'hehe_server'
channel = "chan_107"

###########################pull interval from redis###########################

def pull_config_from_redis():
    print redis.r.keys()
    config_data = redis.r.get("USER:%s" % hostname)
    if config_data is not None:
        config_data = json.loads(config_data)
    else:
        sys.exit('Error: could not find any configuration data on monitor server!!!!')
    return config_data

host_config = pull_config_from_redis()   
#########################client publish data to server###################

def run(service_config):
    service_name, interval, plugin_name = service_config
    plugin_func = getattr(plugin_api,plugin_name)
    res = plugin_func()
    service_data = {
                    'hostname': hostname,
                    'service_name': service_name,
                    'data': res,
                    }
    redis.r.publish(channel, pickle.dumps(service_data) )
    print res


while True:
    for server_name ,v in host_config.items():
        interval, plugin_name, last_time = v
        if (time.time() - last_time )  >= interval:
            t = threading.Thread(target=run, args=( (server_name,v[0],v[1]),    ) )
            t.start()
            host_config[server_name][2] = time.time()
        else:
            next_run_time = interval - ( time.time() - last_time )
            print "\033[32;1m server %s will run in next %s s .. \033[0m" % (server_name, next_run_time)
    time.sleep(1)      
            
            
            
            
                

    
            

