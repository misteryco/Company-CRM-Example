from datetime import datetime

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.test import Client

from faker import Factory
from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee

client = Client()

faker = Factory.create()

User = get_user_model()
username = 'dan'
user_password = '12345'
user_email = "some3@crazy.com"

username_two = 'dan2'
user_password_two = '12345'
user_email_two = "some33@crazy.com"


class SetupForViewsTestsFactory(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username=username,
                                             email=user_email,
                                             password=user_password)
        # self.user.set_password(user_password)
        self.user.save()
        self.sample_user = {
            "username": self.user.username,
            "password": user_password,
            "email": user_email,
            "first_name": "",
            "last_name": ""
        }

        self.user_two = User.objects.create_user(username=username_two,
                                                 email=user_email_two,
                                                 password=user_password_two)
        self.user_two.save()
        self.sample_user_two = {
            "username": self.user_two.username,
            "password": user_password_two,
            "email": user_email_two,
            "first_name": "",
            "last_name": ""
        }

        company_one = Company.objects.create(name=faker.company(),
                                             description=faker.sentence(nb_words=2),
                                             logo='D:/03.jpg',
                                             )
        company_two = Company.objects.create(name=faker.company(),
                                             description=faker.sentence(nb_words=2),
                                             logo='D:/03.jpg',
                                             )
        company_three = Company.objects.create(name=faker.company(),
                                               description=faker.sentence(nb_words=2),
                                               logo='D:/03.jpg',
                                               )
        company_four = Company.objects.create(name=faker.company(),
                                              description=faker.sentence(nb_words=2),
                                              logo='D:/03.jpg',
                                              )
        # for employee in range(10):
        #     employee = Employee.objects.create(first_name=faker.first_name(),
        #                                        last_name=faker.last_name(),
        #                                        date_of_birth=
        #                                        faker.date_between_dates(date_start=datetime(1955, 1, 1),
        #                                                                 date_end=datetime(2001, 12, 31)),
        #                                        photo="D:/03.jpg",
        #                                        position=faker.job(),
        #                                        salary=faker.randomize_nb_elements(number=1000, ge=True, max=10000),
        #                                        company=company_one
        #                                        )

        self.empployee_one = Employee.objects.create(first_name=faker.first_name(),
                                                     last_name=faker.last_name(),
                                                     date_of_birth="2006-07-04",
                                                     photo="D:/03.jpg",
                                                     position="pos 1",
                                                     salary=faker.randomize_nb_elements(number=1000, ge=True,
                                                                                        max=10000),
                                                     company=company_one
                                                     )
        self.empployee_two = Employee.objects.create(first_name=faker.first_name(),
                                                     last_name=faker.last_name(),
                                                     date_of_birth=
                                                     faker.date_between_dates(date_start=datetime(1955, 1, 1),
                                                                              date_end=datetime(2001, 12, 31)),
                                                     photo="D:/03.jpg",
                                                     position=faker.job(),
                                                     salary=faker.randomize_nb_elements(number=1000, ge=True,
                                                                                        max=10000),
                                                     company=company_two
                                                     )
        company_one.owner.set((1,))

        self.company_one = company_one
        self.company_two = company_two

        self.valid_payload = {
            "first_name": "aaa",
            "last_name": "aaa",
            "date_of_birth": "2006-07-04",
            "photo": "/home/yd/Pictures/py/3789820.png",
            "position": "aaa",
            "salary": 100,
            "company": 1
        }

        self.invalid_company_payload = {
            "first_name": "aaa",
            "last_name": "aaa",
            "date_of_birth": "2006-07-04",
            "photo": "/home/yd/Pictures/py/3789820.png",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

        self.invalid_first_name_payload = {
            "first_name": "",
            "last_name": "aaa",
            "date_of_birth": "2006-07-04",
            "photo": "/home/yd/Pictures/py/3789820.png",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

        self.invalid_second_name_payload = {
            "first_name": "aaa",
            "last_name": "",
            "date_of_birth": "2006-07-04",
            "photo": "/home/yd/Pictures/py/3789820.png",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

        self.invalid_date_payload = {
            "first_name": "aaa",
            "last_name": "ooo",
            "date_of_birth": "2020-07-04",
            "photo": "/home/yd/Pictures/py/3789820.png",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }
