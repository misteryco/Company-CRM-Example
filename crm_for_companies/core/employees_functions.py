from datetime import date

from django.core.exceptions import ValidationError
from drf_yasg import openapi

from crm_for_companies.api_companies.models import Company


def validate_age(value):
    min_age_employee = 16
    delta_age = date.today().year - value.year
    if delta_age <= min_age_employee:
        raise ValidationError(
            f"Employee should be at least {min_age_employee} years old"
        )


def get_first_company_pk():
    first_company = Company.objects.all().first()

    if first_company is not None:
        return first_company.pk
    else:
        return None


employee_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "first_name": openapi.Schema(type=openapi.TYPE_STRING),
        "last_name": openapi.Schema(type=openapi.TYPE_STRING),
        "date_of_birth": openapi.Schema(type=openapi.TYPE_STRING),
        "photo": openapi.Schema(type=openapi.TYPE_STRING),
        "position": openapi.Schema(type=openapi.TYPE_STRING),
        "salary": openapi.Schema(type=openapi.TYPE_INTEGER),
        "company": openapi.Schema(type=openapi.TYPE_INTEGER),
    },
    required=[
        "first_name",
        "last_name",
        "date_of_birth",
        "photo",
        "position",
        "salary",
        "company",
    ],
    example={
        "first_name": "FirstName",
        "last_name": "Last",
        "date_of_birth": "2006-07-04",
        "photo": "/home/yd/Pictures/py/3789820.png",
        "position": "NewEmployee",
        "salary": 100,
        "company": get_first_company_pk(),
    },
)
