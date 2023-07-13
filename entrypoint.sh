#!/bin/bash

# Start Celery Workers
celery -A crm_for_companies worker -l info -E &

# Start Celery Beat
celery -A crm_for_companies beat -l info &

# Start Django
python3 manage.py runserver 0.0.0.0:8000