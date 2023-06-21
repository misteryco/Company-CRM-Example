from django.contrib.auth import get_user_model
from rest_framework import status
# from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
# from crm_for_companies.api_employees.serializers import EmployeeSerializerWithCompany
# from crm_for_companies.tests.crm_views.views_setup_employees import TestViewSetupEmployee
from crm_for_companies.tests.crm_views.views_setup_with_factory import SetupForViewsTestsFactory

client = Client()
User = get_user_model()


class TestCreateEmployee(SetupForViewsTestsFactory):

    def test_create_valid_employee(self):
        client.force_login(self.user)
        # Logging and taking user token for not owner user
        response = self.client.post(reverse('api_token_auth'), self.sample_user)
        token = f"Token {response.data['token']}"

        # Authorize client
        self.client.credentials(HTTP_AUTHORIZATION=token)
        # get API response
        # response = self.client.get(reverse('api list employee'))
        response = client.post(
            reverse('api create employee'), self.valid_payload)
        # print(f"2-{response.content}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()
