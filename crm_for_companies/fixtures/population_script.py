import datetime
import os
import random

import django
from django.contrib.auth.hashers import make_password

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "crm_for_companies.settings",
)

django.setup()

# flake8: noqa
"""
Pay attention to where we import the model class. We need to setup our Django setting (line 6–9) before importing it.
 Otherwise, the script won’t run correctly.
 """
from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from django.contrib.auth import get_user_model

UserModel = get_user_model()

NEW_USERS = 10
NEW_COMPANIES = 10
NEW_EMPLOYEES = 5
POSITIONS = ("Boss", "Senior", 'Junior')
SALARY = (1000, 2000, 3000)


def populate_users():
    for i in range(2, NEW_USERS):
        UserModel.objects.create(
            username=f"username_{i}",
            email=f"some_name{i}@domain.nm",
            password=make_password('12345'),
        )


def populate_companies():
    for i in range(2, NEW_COMPANIES):
        Company.objects.create(
            name=f"Company {i}",
            description=f"Simple Company {i} description",
            # logo=date(year=2020, month=3, day=30),
        )


def populate_employees():
    companies = Company.objects.all()

    for company in companies:
        for j in range(2, NEW_EMPLOYEES):
            Employee.objects.create(
                first_name=f"{company.name}_first{j}",
                last_name=f"Last_{j}",
                date_of_birth=datetime.datetime.now() - datetime.timedelta(weeks=52 * random.randint(10, 20)),
                position=random.choice(POSITIONS),
                salary=random.choice(SALARY),
                company=company
            )


if __name__ == "__main__":
    populate_companies()
    populate_employees()
    populate_users()
