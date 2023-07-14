import json

from django.contrib.auth import get_user_model
from rest_framework import status
# from rest_framework.test import APITestCase
from django.test import Client
from django.urls import reverse

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from crm_for_companies.api_employees.serializers import EmployeeSerializerWithCompany
from crm_for_companies.tests.crm_views.views_setup_with_factory import SetupForViewsTestsFactory

client = Client()
User = get_user_model()


class TestEmployeeListView(SetupForViewsTestsFactory):

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


class TestEmployeeSingleView(SetupForViewsTestsFactory):

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


class TestCreateEmployee(SetupForViewsTestsFactory):

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


class UpdateSingleEmployeeTest(SetupForViewsTestsFactory):

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


class DeleteCompanyTest(SetupForViewsTestsFactory):

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
