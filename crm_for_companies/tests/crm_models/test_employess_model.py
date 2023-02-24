from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee
from django.test import TestCase
from django.core.exceptions import ValidationError


class TestCompanyModel(TestCase):
    company = Company(
        name='12345',
        description='A new company 1 description',
        logo='D:/03.jpg',
    )
    employee = Employee(
        first_name="aaaaaaa",
        last_name="aaaaaaa",
        date_of_birth="2006-07-04",
        photo="D:/03.jpg",
        position="aaa",
        salary=100,
        company=company
    )

    def test_user_model_when_LAST_name_is_too_short__expect_exception(self):
        self.company.save()
        self.employee.last_name = "1"
        self.employee.company = self.company

        with self.assertRaises(ValidationError) as context:
            self.employee.full_clean()
            self.employee.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_FIRST_name_is_too_short__expect_exception(self):
        self.company.save()
        self.employee.first_name = "1"
        self.employee.last_name = "12345"
        self.employee.company = self.company

        with self.assertRaises(ValidationError) as context:
            self.employee.full_clean()
            self.employee.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_age_is_less_than_necessary__expect_exception(self):
        self.company.save()
        self.employee.date_of_birth = "2020-07-04"
        self.employee.company = self.company

        with self.assertRaises(ValidationError) as context:
            self.employee.full_clean()
            self.employee.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_age_is_good__expect_exception(self):
        self.company.save()
        self.employee.company = self.company
        self.employee.first_name = "12345"
        self.employee.last_name = "12345"
        self.employee.full_clean()  # Call this for validation
        self.employee.save()

        self.assertIsNotNone(self.employee.pk)
