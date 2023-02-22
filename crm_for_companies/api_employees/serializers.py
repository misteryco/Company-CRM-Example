from rest_framework import serializers

from crm_for_companies.api_companies.serializers import ShortCompanySerializer
from crm_for_companies.api_employees.models import Employee


class EmployeeSerializerWithCompany(serializers.ModelSerializer):
    # Give more than ID for company
    company = ShortCompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        instance.photo = instance.photo.url
        new_representation = super().to_representation(instance)

        return new_representation


class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
