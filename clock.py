from apscheduler.schedulers.blocking import BlockingScheduler 

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def test_job():
    print('Test job runs every minute')
    
sched.start()
