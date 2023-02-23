from crm_for_companies.api_companies.models import Company
from django.test import TestCase
from django.core.exceptions import ValidationError


class TestCompanyModel(TestCase):
    company = Company(
        name='12345',
        description='A new company 1 description',
        logo='D:/03.jpg',
    )

    def test_user_model_when_name_is_too_short__expect_exception(self):
        self.company.name = "1"

        with self.assertRaises(ValidationError) as context:
            self.company.full_clean()
            self.company.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_name_is_fine__expect_normal(self):
        self.company.name = "12345"

        self.company.full_clean()  # Call this for validation
        self.company.save()

        self.assertIsNotNone(self.company.pk)

    def test_user_model_when_description_is_too_short__expect_exception(self):
        self.company.description = "1"

        with self.assertRaises(ValidationError) as context:
            self.company.full_clean()
            self.company.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_description_is_fine__expect_normal(self):
        self.company.description = "1234567890"

        self.company.full_clean()  # Call this for validation
        self.company.save()

        self.assertIsNotNone(self.company.pk)