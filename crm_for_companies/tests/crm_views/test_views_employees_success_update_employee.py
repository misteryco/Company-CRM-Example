import json

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from crm_for_companies.api_employees.serializers import EmployeeSerializerWithCompany

client = Client()


class UpdateSingleEmployeeTest(TestCase):

    def setUp(self):
        username = 'dan'
        user_password = 'KsijdyY^sd768A'
        User = get_user_model()

        self.user = User.objects.create_user(username=username, )
        self.user.set_password(user_password)
        self.user.save()

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

        self.empployee_one = Employee.objects.create(first_name="Employee 1",
                                                     last_name="1",
                                                     date_of_birth="2006-07-04",
                                                     photo="D:/03.jpg",
                                                     position="pos 1",
                                                     salary=100,
                                                     company=self.company_one
                                                     )
        self.empployee_two = Employee.objects.create(first_name="Employee 1",
                                                     last_name="1",
                                                     date_of_birth="2006-07-04",
                                                     photo="D:/03.jpg",
                                                     position="pos 1",
                                                     salary=100,
                                                     company=self.company_two
                                                     )
        self.valid_payload = {
            "id": 1,
            "first_name": "Spas",
            "last_name": "LastName",
            "date_of_birth": "2000-02-03",
            "position": "HR",
            "photo": "",
            "salary": 1,
            "company": 1
        }

        self.invalid_company_payload = {
            "first_name": "aaa",
            "last_name": "aaa",
            "date_of_birth": "2006-07-04",
            "photo": "D:/03.jpg",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

        self.invalid_first_name_payload = {
            "first_name": "",
            "last_name": "aaa",
            "date_of_birth": "2006-07-04",
            "photo": "D:/03.jpg",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

        self.invalid_second_name_payload = {
            "first_name": "aaa",
            "last_name": "",
            "date_of_birth": "2006-07-04",
            "photo": "D:/03.jpg",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

        self.invalid_date_payload = {
            "first_name": "aaa",
            "last_name": "ooo",
            "date_of_birth": "2020-07-04",
            "photo": "D:/03.jpg",
            "position": "aaa",
            "salary": 100,
            "company": 42
        }

    def test_update_valid_employee(self):
        response = client.put(
            reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
