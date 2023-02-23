from django.test import TestCase, Client
from rest_framework.authtoken.admin import User

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee


class CRMApiTestCase(TestCase):
    username = 'dan1'
    user_password = '111'

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username=self.username,
            password=self.user_password,
        )
        self.create_company = Company(
            name='My company1',
            description='A new company 1 description',
            logo='D:/03.jpg',
        )
        self.create_company = Company(
            name='My company2',
            description='A new company 2 description',
            logo='D:/03.jpg',
        )
        self.create_employee = Employee(
            first_name="FirstName1",
            last_name="LastName1",
            date_of_birth="2019-07-04",
            photo="D:/03.jpg",
            position="Position 1",
            salary=100,
            company=1,
        )
