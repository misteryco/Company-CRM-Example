from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializerWithEmployees
from crm_for_companies.api_employees.models import Employee

client = Client()


class TestCompanyListView(APITestCase):

    def setUp(self):
        username = 'dan'
        user_password = '12345'
        user_email = "some3@crazy.com"
        User = get_user_model()

        self.user = User.objects.create_user(username=username, email=user_email, password=user_password)
        # self.user.set_password(user_password)
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

    def test_get_all_companies(self):
        # Logging user
        client.force_login(self.user)

        # Taking logged user token
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)

        # get API response
        response = self.client.get(reverse('api list company'))

        # Get data from db
        companies = Company.objects.all()
        serializer = CompanySerializerWithEmployees(companies, many=True)

        # Test response:
        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_companies_no_authentication(self):
        response = self.client.get(reverse('api list company'))
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

























# class TestCompany(APITestCase):
#     def test_auth_user_name(self):
#         sample_user = {
#             "username": "SomeOneNew3",
#             "password": "12345",
#             "email": "some3@crazy.com",
#             "first_name": "",
#             "last_name": ""
#         }
#
#         # Here we send a request 'register_user' and response is saved in :
#         # this an actual request/response cycle
#         response = self.client.post(reverse('register_user'), sample_user)
#         # print(str(response))
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # print("Bliah")
#         response = self.client.post(reverse('api_token_auth'), {"username": "SomeOneNew3", "password": "12345"})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         token = f"Token {response.data['token']}"
#
#         self.client.credentials(HTTP_AUTHORIZATION=token)
#
#         response = self.client.get(reverse('get user by token'))
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         self.assertJSONEqual(response.content.decode("utf-8"), {"userNameByToken": "SomeOneNew3"})
