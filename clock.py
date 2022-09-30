from apscheduler.schedulers.blocking import BlockingScheduler 
import psycopg2
import time 
from datetime import datetime   

sched = BlockingScheduler()

#current_time = now.strftime("%H:%M:%S:%s")
connection_url_1 = "postgres://uegd5r8smr61qd:p7d5e85bbb056492032d33191fd1690e9b175046a283a2a4a72691f6322e63ebb@ec2-3-222-180-4.compute-1.amazonaws.com:5432/d2v27nidm8glbg"
connection_url = "postgres://u7r96o31vp2hlk:pae99a023860272fca7f1e2af513f5611e66ce6437db3934837fe732eb9ecbc6e@ec2-54-210-170-57.compute-1.amazonaws.com:5432/dnvab2bl745rg"
status = False

@sched.scheduled_job('interval', minutes=2)
def test_job():
    print('Test job runs every 2 minutes')
    
@sched.scheduled_job('interval', minutes=2)
def check_connection():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%s")
    #last_succes_conn = 0
    last_fail_begin = 0 
    #last_fail_end = 0
    name = "DB1"
    #global status
    #if (status==False) :
        #connection_url= connection_url
    try:
        conn = psycopg2.connect(connection_url)
        print(f"Connection to {name} succesful at {current_time}")
        last_fail_begin == 0
        status = True
        return last_fail_begin
    except:
        #print(f"Connection to {name} failure {current_time}")
        if (last_fail_begin == 0):
            last_fail_begin = current_time
            print(f"Connection to {name} failure at {last_fail_begin}")
        else:
            print(f"{name} down since {last_fail_begin}. Retrying connection")
        status = False
        return status
    
        
        

    #conn.close()
    #print("Connection to closed at ", current_time)
        

    
sched.start()
