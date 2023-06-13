import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_for_companies.settings')

app = Celery('crm_for_companies')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Following row load task modules from all registered Django app configs.
app.autodiscover_tasks()


# To start celery use following command:
# celery -A crm_for_companies worker -l info -E
# First run Celery, then run server


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
