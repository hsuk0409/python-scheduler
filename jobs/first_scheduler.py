import schedule

def job():
    print("schedule test!!")

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
