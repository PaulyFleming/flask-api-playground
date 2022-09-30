from apscheduler.schedulers.blocking import BlockingScheduler 
import psycopg2
import time 
from datetime import datetime   

sched = BlockingScheduler()
now = datetime.now()
current_time = now.strftime("%H:%M:%S:%s")
connection_url = "postgres://u7r96o31vp2hlk:pae99a023860272fca7f1e2af513f5611e66ce6437db3934837fe732eb9ecbc6e@ec2-54-210-170-57.compute-1.amazonaws.com:5432/dnvab2bl745rg"

@sched.scheduled_job('interval', minutes=3)
def test_job():
    print('Test job runs every minute')
    
@sched.scheduled_job('interval', seconds=15)
def check_connection():
    name = "DB1"
    #connection_url= connection_url
    try:
        conn = psycopg2.connect(connection_url)
        print(f"Connection to {name} succesful at ", current_time)
    except:
        print("Connection failure at ", current_time)
        
    for x in range(5): 
        time.sleep(0.5)
        print("...")

    conn.close()
    print("Connection closed at ", current_time)
        

    
sched.start()
