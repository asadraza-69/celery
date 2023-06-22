import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE','testing.settings')

app = Celery('testing')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# broker_connection_retry_on_startup = True

# app.conf.beat_schedule = {
#     'add-every-5-seconds': {
#         'task': 'vubon',
#         'schedule': 5.0,
#     },
#     'add-every-minute-contrab': {
#         'task': 'data_checking',
#         'schedule': crontab(minute=1),
#     },
# }