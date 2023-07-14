from datetime import date

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import MinLengthValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
# from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator

# from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_companies.serializers import ShortCompanySerializer
from crm_for_companies.api_employees.models import Employee


def validate_age(value):
    min_age_employee = 16
    delta_age = date.today().year - value.year
    # print(f"delta_age={delta_age}")
    if delta_age <= min_age_employee:
        raise ValidationError(f'Employee should be at least {min_age_employee} years old')


class EmployeeSerializerWithCompany(serializers.ModelSerializer):
    company = ShortCompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'


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

    def to_representation(self, instance):
        instance.photo = instance.photo
        # instance.logo = instance.logo.url
        new_representation = super().to_representation(instance)

        return new_representation


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    # password2 = serializers.CharField(write_only=True, required=True)
    # same password validation should be done in the frontend

    class Meta:
        model = User
        # fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #
    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])

        user.save()

        return user
