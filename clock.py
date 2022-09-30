from apscheduler.schedulers.blocking import BlockingScheduler 
import psycopg2
import time 
from datetime import datetime   

sched = BlockingScheduler()

#current_time = now.strftime("%H:%M:%S:%s")
connection_url = "postgres://u7r96o31vp2hlk:pae99a023860272fca7f1e2af513f5611e66ce6437db3934837fe732eb9ecbc6e@ec2-54-210-170-57.compute-1.amazonaws.com:5432/dnvab2bl745rg"
status = False

@sched.scheduled_job('interval', minutes=2)
def test_job():
    print('Test job runs every 2 minutes')
    
@sched.scheduled_job('interval', seconds=15)
def check_connection():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%s")
    name = "DB1"
    try:
        conn = psycopg2.connect(connection_url, connect_timeout=7)
        print(f"Connection to {name} succesful at {current_time}")

    except:
        print(f"Connection to {name} failure at {current_time}")

        

    
sched.start()
