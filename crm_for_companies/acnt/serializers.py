from rest_framework import serializers

from crm_for_companies.acnt.models import AppUser


class CreateAppUser(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('username', 'password',)
