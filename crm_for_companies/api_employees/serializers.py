from datetime import date

from cloudinary.cache.responsive_breakpoints_cache import instance
from django.core.validators import MinLengthValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import PrimaryKeyRelatedField

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import ShortCompanySerializer
from crm_for_companies.api_employees.models import Employee


def validate_age(value):
    min_age_employee = 16
    delta_age = date.today().year - value.year
    # print(f"delta_age={delta_age}")
    if delta_age <= min_age_employee:
        raise ValidationError(f'Employee should be at least {min_age_employee} years old')


class EmployeeSerializerWithCompany(serializers.ModelSerializer):
    # Give more than ID for company
    company = ShortCompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    # def to_representation(self, instance):
    #     print(instance.company)
    #     instance.photo = instance.photo.url
    #     new_representation = super().to_representation(instance)
    #
    #     return new_representation


class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    first_name = serializers.CharField(max_length=Employee.NAME_MAX_LEN,
                                       validators=[MinLengthValidator(Employee.NAME_MIN_LEN), ])

    last_name = serializers.CharField(max_length=Employee.NAME_MAX_LEN,
                                      validators=[MinLengthValidator(Employee.NAME_MIN_LEN), ])

    date_of_birth = serializers.DateField(validators=(validate_age,), )

    position = serializers.CharField(max_length=Employee.POSITION_MAX_LEN,
                                     validators=[MinLengthValidator(Employee.POSITION_MIN_LEN), ])
