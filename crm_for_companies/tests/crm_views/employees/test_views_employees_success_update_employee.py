import json

from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee

from crm_for_companies.tests.crm_views.views_setup_with_factory import SetupForViewsTestsFactory

client = Client()
User = get_user_model()


class UpdateSingleEmployeeTest(SetupForViewsTestsFactory):

    def test_update_valid_employee(self):
        response = client.put(
            reverse('api update employee', kwargs={'pk': self.empployee_one.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        # print(f"3 - {response.content}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        Employee.objects.all().delete()
        Company.objects.all().delete()
        User.objects.all().delete()
