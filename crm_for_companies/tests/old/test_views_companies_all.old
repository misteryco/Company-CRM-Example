from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company, UserModel
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


class TestCompanyCreateView(APITestCase):

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

    def test_post_company(self):
        # Logging user
        client.force_login(self.user)

        # Taking logged user token
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)

        # get API response
        response = self.client.post(reverse(
            'api create company'),
            {
                "name": "ComXXXX111",
                "description": "Some data mor1111",
                "logo": "/home/yd/Screenshot-10.png",
                "owner": [1]
            }
        )

        # Get data from db
        new_company = Company.objects.filter(name="ComXXXX111").get()

        # Test response:
        self.assertEqual(response.data['status'], 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['name'], new_company.name)

    def test_get_all_companies_no_authentication(self):
        response = self.client.get(reverse('api list company'))
        self.assertEqual(response.data['detail'], "Authentication credentials were not provided.")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestCompanyDetailsView(APITestCase):

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

    def test_get_company_by_pk(self):
        # Logging user
        # client.force_login(self.user)

        # Taking logged user token
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)

        # get API response
        response = self.client.get(reverse('api details company', kwargs={'pk': self.company_one.pk}))

        # Get data from db
        company_data = Company.objects.filter(pk=self.company_one.pk).get()
        # UserModel.objects.filter(company__owner=self.user)

        # Test response:
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], company_data.name)

    def test_get_company_data_user_is_not_owner(self):
        # Logging and taking user token for not owner user
        response = self.client.post(reverse('api_token_auth'), self.sample_user_two)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)

        # get API response
        response = self.client.get(reverse('api details company', kwargs={'pk': self.company_two.pk}))

        # Test response:
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data['detail'], "Only Owner can see company details.")

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
