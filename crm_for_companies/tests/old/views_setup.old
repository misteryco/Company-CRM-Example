from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.test import Client

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee

client = Client()


class SetupFoRViewsTests(APITestCase):

    def setUp(self):
        username = 'dan'
        user_password = '12345'
        user_email = "some3@crazy.com"
        User = get_user_model()

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

        username_two = 'dan2'
        user_password_two = '12345'
        user_email_two = "some33@crazy.com"

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

        company_one = Company.objects.create(name='Company 1',
                                             description='A new company 1 description',
                                             logo='D:/03.jpg',
                                             )
        company_two = Company.objects.create(name='Company 2',
                                             description='A new company 2 description',
                                             logo='D:/03.jpg',
                                             )
        company_three = Company.objects.create(name='Company 3',
                                               description='A new company 3 description',
                                               logo='D:/03.jpg',
                                               )
        company_four = Company.objects.create(name='Company 4',
                                              description='A new company 4 description',
                                              logo='D:/03.jpg',
                                              )
        empployee_one = Employee.objects.create(first_name="Employee 1",
                                                last_name="1",
                                                date_of_birth="2006-07-04",
                                                photo="D:/03.jpg",
                                                position="pos 1",
                                                salary=100,
                                                company=company_one
                                                )
        empployee_two = Employee.objects.create(first_name="Employee 1",
                                                last_name="1",
                                                date_of_birth="2006-07-04",
                                                photo="D:/03.jpg",
                                                position="pos 1",
                                                salary=100,
                                                company=company_two
                                                )
        company_one.owner.set((1,))

        self.company_one = company_one
        self.company_two = company_two
