import os
from celery import Celery

from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_for_companies.settings')

app = Celery('crm_for_companies')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'add-every-2-seconds': {
        # task that you want to be scheduled
        'task': 'crm_for_companies.api_employees.tasks.print_messages',
        # Fist way to define schedule: just seconds
        'schedule': 2,

        # Second way to define schedule: crontab
        # 'schedule': crontab(),
        # crontab() - Execute every minute;
        # crontab(minute='*', hour='*', day_of_week='sun')  - Execute "every minute" at Sundays

        'args': ('This is sample message.',)
    }
}

# Following row load "tasks.py" modules from all registered Django app configs.
app.autodiscover_tasks()

# To start celery use following command:
# celery -A crm_for_companies worker -l info -E
# To start scheduled beat functions use following command:
# ! It's good to use a second terminal window !
# celery -A crm_for_companies beat -l info
# First run Celery, then run server

# If you want only one worker use:
#  celery -A crm_for_companies worker -c 1

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
