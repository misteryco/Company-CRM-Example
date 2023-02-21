from rest_framework import serializers

from crm_for_companies.api_employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        instance.photo = instance.photo.url
        new_representation = super().to_representation(instance)

        return new_representation
