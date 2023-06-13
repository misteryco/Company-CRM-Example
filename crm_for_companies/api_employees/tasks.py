import logging
import time

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
