from rest_framework import serializers

from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee


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
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        # print(f"serializer logo data : {instance.logo}")
        # print(f"serializer logo data : {instance.logo.url}")
        instance.logo = instance.logo.url
        new_representation = super().to_representation(instance)

        return new_representation


class CompanyCustomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
