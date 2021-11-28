import time

from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler


class TestApScheduler:

    def __init__(self):
        self.back_scheduler_obj = BackgroundScheduler()
        self.back_scheduler_obj.start()
        self.job_id = ""

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        self.back_scheduler_obj.shutdown()

    def kill_scheduler(self, job_id):
        try:
            self.back_scheduler_obj.remove_job(job_id=job_id)
        except JobLookupError as e:
            print(f"fail to stop scheduler: {e}")
            return

    def hello(self, job_type, job_id):
        print(f"{job_type} Scheduler process_id[{job_id}] : {time.localtime().tm_sec}")

    def scheduler(self, job_type, job_id):
        print(f"{job_type} Scheduler Start")
        if job_type == "interval":
            self.back_scheduler_obj.add_job(self.hello, job_type, seconds=10, id=job_id, args=(job_type, job_id))
        elif job_type == "cron":
            self.back_scheduler_obj.add_job(self.hello, job_type, day_of_week="mon-fri",
                                            hour="0-23", second="*/2", id=job_id, args=(job_type, job_id))


if __name__ == "__main__":
    scheduler = TestApScheduler()
    scheduler.scheduler("cron", "1")
    scheduler.scheduler("interval", "2")

    count = 0
    while True:
        print("Running main process")
        time.sleep(1)

        count += 1
        if count == 10:
            scheduler.kill_scheduler("1")
            print("Kill cron scheduler")
        elif count == 15:
            scheduler.kill_scheduler("2")
            print("Kill interval scheduler")
