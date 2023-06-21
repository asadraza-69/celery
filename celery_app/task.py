from celery import shared_task
from time import sleep

@shared_task
def sleep_fun(duration):
    sleep(duration)
    return f"Task completed. Duration: {duration} seconds"
