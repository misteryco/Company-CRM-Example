import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.decorators import api_view

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import CompanySerializerWithEmployees, CompanySerializer
from crm_for_companies.api_employees.models import Employee

client = Client()


class TestCompanyListView(TestCase):

    def setUp(self):
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

    def test_get_all_companies_with_employees(self):
        # get API response
        response = client.get(reverse('api list company'))
        # get data from db
        companies = Company.objects.all()
        serializer = CompanySerializerWithEmployees(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCompanySingleView(TestCase):
    client = Client()

    # initialize the APIClient app
    def setUp(self):
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

    def test_get_details_company(self):
        response = client.get(
            reverse('api details company', kwargs={'pk': self.company_one.pk}))
        company = Company.objects.get(pk=self.company_one.pk)
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCreateCompany(TestCase):
    client = Client()

    # initialize the APIClient app
    def setUp(self):
        self.valid_payload = {'name': 'Company 1',
                              'description': 'A new company 1 description',
                              'logo': 'D:/03.jpg'
                              }

        self.invalid_payload = {'name': '',
                                'description': 'A new company 1 description',
                                'logo': 'D:/03.jpg'
                                }

    def test_create_valid_company(self):
        response = client.post(
            reverse('api create company'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_company(self):
        response = client.post(
            reverse('api create company'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleCompanyTest(TestCase):

    def setUp(self):
        self.company_one = Company.objects.create(name='Company 1',
                                                  description='A new company 1 description',
                                                  logo='D:/03.jpg',
                                                  )
        self.company_two = Company.objects.create(name='Company 2',
                                                  description='A new company 2 description',
                                                  logo='D:/03.jpg',
                                                  )
        self.valid_payload = {'name': 'Company 1',
                              'description': 'A new company 1 description',
                              'logo': 'D:/03.jpg'
                              }

        self.invalid_payload = {'name': '',
                                'description': 'A new company 1 description',
                                'logo': 'D:/03.jpg'
                                }

    def test_valid_update_company(self):
        response = client.put(
            reverse('api details company', kwargs={'pk': self.company_one.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_company(self):
        response = client.put(
            reverse('api details company', kwargs={'pk': self.company_one.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteCompanyTest(TestCase):

    def setUp(self):
        self.company_one = Company.objects.create(name='Company 1',
                                                  description='A new company 1 description',
                                                  logo='D:/03.jpg',
                                                  )
        self.company_two = Company.objects.create(name='Company 2',
                                                  description='A new company 2 description',
                                                  logo='D:/03.jpg',
                                                  )

    def test_valid_delete_company(self):
        response = client.delete(
            reverse('api details company', kwargs={'pk': self.company_two.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_company(self):
        response = client.delete(
            reverse('api details company', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
