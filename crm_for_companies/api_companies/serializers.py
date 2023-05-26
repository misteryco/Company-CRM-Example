from django.core.validators import MinLengthValidator
from rest_framework import serializers

from crm_for_companies.api_companies.models import Company, UserModel
from crm_for_companies.api_employees.models import Employee


class ShortUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('pk', 'username',)


class ShortEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', ]


class ShortCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'logo')

    def to_representation(self, instance):
        instance.logo = instance.logo.url
        new_representation = super().to_representation(instance)

        return new_representation


class CompanySerializerWithEmployees(serializers.ModelSerializer):
    employee_set = ShortEmployeeSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        instance.logo = instance.logo.url
        new_representation = super().to_representation(instance)

        return new_representation


class CompanySerializer(serializers.ModelSerializer):
    owner = ShortUserSerializer(many=True)

    class Meta:
        model = Company
        fields = '__all__'

    name = serializers.CharField(max_length=Company.NAME_MAX_LEN,
                                 validators=[MinLengthValidator(Company.NAME_MIN_LEN), ])

    description = serializers.CharField(max_length=Company.DESCRIPTION_MAX_LENGTH,
                                        validators=[MinLengthValidator(Company.DESCRIPTION_MIN_LENGTH), ])

    def to_representation(self, instance):
        instance.logo = instance.logo
        # list_of_owners = [obj.username for obj in instance.owner.all()]
        # print(list_of_owners)
        # instance.logo = instance.logo.url
        new_representation = super().to_representation(instance)

        return new_representation


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    name = serializers.CharField(max_length=Company.NAME_MAX_LEN,
                                 validators=[MinLengthValidator(Company.NAME_MIN_LEN), ])
