from cloudinary.templatetags import cloudinary as cloudinary_template_tags
from rest_framework import serializers

from crm_for_companies.api_companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def to_representation(self, instance):
        instance.logo = instance.logo.url
        new_representation = super().to_representation(instance)

        return new_representation
