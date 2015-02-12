import global_setting
from conf import hosts
import redis_connecter as redis
import json , time
import pickle
channel = "chan_107"
##########################server push interval  to redis ####################

    
def push_config_data_to_redis():    
    for h in hosts.monitor_lists:
        config_dic = { }
        for k ,v in h.services.items():
            config_dic[k] = [v.interval , v.plugin_name, 0]  # zero time
        redis.r['USER:%s' % h.hostname] = json.dumps(config_dic)

push_config_data_to_redis()

#######################server subscribe  data from redis server###############################
msg_queue = redis.r.pubsub()
msg_queue.subscribe(channel)
msg_queue.parse_response()

count = 0 
while True:
    data = msg_queue.parse_response()
    recived_dic = pickle.loads(data[2])
    recived_dic['recv_time'] = time.time()
    print 'round %s :::: '  % count, recived_dic
    redis_key =   "%s::%s"  %  ( recived_dic['hostname'], recived_dic['service_name'] )
    print "###################" , redis_key
    redis.r[redis_key] = json.dumps(recived_dic) 
    for k ,v in recived_dic.items():
       print " %s ------------> %s"  % (k ,v) 
    count+= 1
    
    
    

