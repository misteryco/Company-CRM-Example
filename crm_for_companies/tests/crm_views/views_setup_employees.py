from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from crm_for_companies.api_companies.models import Company


class TestViewSetupEmployee(APITestCase):
    def setUp(self):
        User = get_user_model()
        username = 'dan'
        user_password = '12345'
        user_email = "some3@crazy.com"

        self.user = User.objects.create_user(username=username,
                                             email=user_email,
                                             password=user_password)
        self.user.set_password(user_password)
        self.user.save()

        self.sample_user = {
            "username": self.user.username,
            "password": user_password,
            "email": user_email,
            "first_name": "",
            "last_name": ""
        }
        self.company_one = Company.objects.create(name='Company 1',
                                                  description='A new company 1 description',
                                                  logo='D:/03.jpg',
                                                  )
        self.company_two = Company.objects.create(name='Company 2',
                                                  description='A new company 2 description',
                                                  logo='D:/03.jpg',
                                                  )
        self.company_three = Company.objects.create(name='Company 3',
                                                    description='A new company 3 description',
                                                    logo='D:/03.jpg',
                                                    )
        self.company_four = Company.objects.create(name='Company 4',
                                                   description='A new company 4 description',
                                                   logo='D:/03.jpg',
                                                   )
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
