from rest_framework import status
from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.tests.crm_views.test_views_setup import SetupFoRViewsTests
from crm_for_companies.tests.crm_views.test_views_setup_with_factory import SetupFoRViewsTestsFactory

client = Client()


class TestCompanyDetailsView(SetupFoRViewsTestsFactory):

    def test_get_company_by_pk(self):
        # Authenticate user and get Token
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
        self.company_one.owner.clear()
