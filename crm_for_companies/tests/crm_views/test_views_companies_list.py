from rest_framework import status
from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializerWithEmployees
from crm_for_companies.tests.crm_views.test_views_setup import SetupFoRViewsTests
from crm_for_companies.tests.crm_views.test_views_setup_with_factory import SetupFoRViewsTestsFactory

client = Client()


class TestCompanyListView(SetupFoRViewsTestsFactory):

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
