import logging
import time
from datetime import datetime

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email_to_new_users(name, email):
    time.sleep(60)
    send_mail(subject='Wellcome from CRM For Companies',
              message=f"Welcome {name} with {email}",
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=(email,))
    logging.info(f"Welcome email was send to {name} with {email}")


@shared_task
def sum_a_b(a, b):
    time.sleep(7)
    return a + b


@shared_task
def print_messages(message):
    time.sleep(10)
    print(f"Time form scheduled task: {datetime.now().time()}. Additional argument: {message}")
