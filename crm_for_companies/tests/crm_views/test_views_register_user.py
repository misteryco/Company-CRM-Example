from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from crm_for_companies.tests.crm_views.views_setup_with_factory import SetupForViewsTestsFactory

client = Client()
User = get_user_model()


# flake8: noqa
class TestCompanyListView(SetupForViewsTestsFactory):
    def test_take_token_for_existing_user_success(self):
        # Taking existing user token
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()

    def test_get_ID_for_existing_user_success(self):
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Get user by token
        self.client.credentials(HTTP_AUTHORIZATION=token)
        response = self.client.get(reverse('get user by token'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()
