from django.contrib.auth import get_user_model
from rest_framework import status

from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from crm_for_companies.tests.crm_views.views_setup_with_factory import SetupForViewsTestsFactory

client = Client()

User = get_user_model()


class TestCompanyCreateView(SetupForViewsTestsFactory):

    def test_post_company(self):
        # Taking logged user token
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)

        # get API response
        response = self.client.post(
            reverse
            ('api create company'),
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

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()
