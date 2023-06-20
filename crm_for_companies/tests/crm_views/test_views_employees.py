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
User = get_user_model()


class TestEmployeeListView(APITestCase):

    def setUp(self):
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

    def test_get_all_employees_with_employees(self):
        client.force_login(self.user)
        # Logging and taking user token for not owner user
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)
        # get API response
        response = self.client.get(reverse('api list employee'))
        # get data from db
        # employees = Employee.objects.all()
        # serializer = EmployeeSerializerWithCompany(employees, many=True)
        # self.assertEqual(response.data['data'], serializer.data)
        # self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()


class TestEmployeeSingleView(TestCase):

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

    def test_get_details_employee_success(self):
        client.force_login(self.user)
        response = client.get(
            reverse('api details employee', kwargs={'pk': self.empployee_one.pk}))
        employee = Employee.objects.get(pk=self.empployee_one.pk)
        serializer = EmployeeSerializerWithCompany(employee)

        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_details_employee_NOT_success(self):
        client.force_login(self.user)
        response = client.get(
            reverse('api details employee', kwargs={'pk': 1000}))

        self.assertEqual(response.data['status'], 404)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()


class TestCreateEmployee(APITestCase):
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

    # def test_create_valid_employee(self):
    #     client.force_login(self.user)
    #     # Logging and taking user token for not owner user
    #     response = self.client.post(reverse('api_token_auth'), self.sample_user)
    #     token = f"Token {response.data['token']}"
    #
    #     # Authorize client
    #     self.client.credentials(HTTP_AUTHORIZATION=token)
    #     # get API response
    #     # response = self.client.get(reverse('api list employee'))
    #     response = client.post(
    #         reverse('api create employee'), self.valid_payload)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company_employee(self):
        client.force_login(self.user)
        response = client.post(
            reverse('api create employee'),
            data=json.dumps(self.invalid_company_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_first_name_employee(self):
        client.force_login(self.user)
        response = client.post(
            reverse('api create employee'),
            data=json.dumps(self.invalid_first_name_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_second_name_employee(self):
        client.force_login(self.user)
        response = client.post(
            reverse('api create employee'),
            data=json.dumps(self.invalid_second_name_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_date_employee(self):
        client.force_login(self.user)
        response = client.post(
            reverse('api create employee'),
            data=json.dumps(self.invalid_date_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()


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
            "first_name": "aaa",
            "last_name": "aaa",
            "date_of_birth": "2006-07-04",
            "photo": "D:/03.jpg",
            "position": "aaa",
            "salary": 100,
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

    #
    # def test_update_valid_employee(self):
    #     client.force_login(self.user)
    #     response = client.put(
    #         reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
    #         data=json.dumps(self.valid_payload),
    #         content_type='application/json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_company_employee(self):
        client.force_login(self.user)
        response = client.put(
            reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
            data=json.dumps(self.invalid_company_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_first_name_employee(self):
        client.force_login(self.user)
        response = client.put(
            reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
            data=json.dumps(self.invalid_first_name_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_second_name_employee(self):
        client.force_login(self.user)
        response = client.put(
            reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
            data=json.dumps(self.invalid_second_name_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_invalid_date_employee(self):
        client.force_login(self.user)
        response = client.put(
            reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
            data=json.dumps(self.invalid_date_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()


class DeleteCompanyTest(TestCase):

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

    def test_valid_delete_employee(self):
        client.force_login(self.user)
        response = client.delete(
            reverse('api delete employee', kwargs={'pk': self.empployee_one.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_employee(self):
        client.force_login(self.user)
        response = client.delete(
            reverse('api delete employee', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()
