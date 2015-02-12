#! /usr/bin/env python
import global_setting
from conf import hosts
import redis_connecter as redis
import json, time

def fetch_monitor_lists():
    for h in hosts.monitor_lists:
        print '\033[42;1m -------------------------------%s----------------------------------\033[0m'  % h.hostname
        for service_name ,v in h.services.items():
            redis_key = "%s::%s" % (h.hostname , service_name )
            service_data = redis.r.get(redis_key)
            if service_data is not None:
                service_data = json.loads(service_data)
                    # print service_data
                time_pass_since_last_recv = time.time() - service_data["recv_time"]
                print "time pass::" , time_pass_since_last_recv
                if time_pass_since_last_recv > v.interval +10 :
                    print "\033[41;1m-------------------can not recive any data now------------------\033[0m"
                
                else: #data send from client on time
                    if service_data['data']['status'] == 0:
                        for index, val in v.triggers.items():
                            print '===========>',"default:", index, val
                            data_type,  warning, critical = val
                            index_val = service_data['data'][index]
                            if data_type == 'percentage' or data_type is int:
                                index_val = float(index_val)
                                
                            #add index value into temp_data dic
                            if service_data["recv_time"] != v.temp_data[index]['time']: 
                                 #to make sure save userful data
                                v.temp_data[index]['status_data'].append(index_val)
                                #to update time
                                v.temp_data[index]['time'] = service_data["recv_time"]
                            #make sure temp data list has no more than 10 nums
                            if len(v.temp_data[index]['status_data']) > 10:
                                del v.temp_data[index]['status_data'][0]
                            
                            #loop temp data list to check how many nums have crossed critical
                            cross_warning_count = 0
                            cross_critical_count = 0
                          
                            for items in  v.temp_data[index]['status_data']:                              
                            # compare parts
                                if index in v.It_operator:      
                                    if float(items) < float(critical):
                                        print "\033[31;1m Service %s crossed critical line %s, current value is %s\033[0m" % (index, critical, items)
                                        cross_critical_count +=1
                                    elif float(items) < float(warning):
                                        print "\033[31;1m Service %s crossed warning line %s, current value is %s\033[0m"  % (index, warning, items)
                                        cross_warning_count +=1
                                else: 
                                    if float(items) > float(critical):
                                        print "\033[31;1mService %s crossed critical line %s, current value is %s\033[0m" % (index, critical, items)
                                        cross_critical_count +=1
                                    elif float(items) > float(warning):
                                        print "\033[31;1m Service %s crossed warning line %s, current value is %s\033[0m"  % (index, warning, items)  
                                        cross_critical_count +=1
                                
                                
                                print "\033[44;1m------------------temp data length-------------------\033[0m", service_name ,index, v.temp_data[index]['status_data']
                                print "--------------------------Warning count:", cross_warning_count
                                
                                print "--------------------------Critical count:", cross_critical_count
                                while cross_critical_count > 5:
                                    return_value = {"hostname" :h.hostname,"service_name": service_name,"trigger":index,"status": "critical"}
                                    return   return_value
                                
                             #OK, if your get (cross_warning_count  > 5) or (cross_critical_count > 5), we should use send_mail.py. 
                            
                            
                    else:
                        print "033[31;1m%s  data is not vaild\033[0m" %  service_name , service_data
                                                                
            else:
                print '\033[43;1m ---------%s do not send data forever--------\033[0m'  % h.hostname
                


if __name__ == "__main__":
    while True:
        fetch_monitor_lists()
        time.sleep(1)
                
