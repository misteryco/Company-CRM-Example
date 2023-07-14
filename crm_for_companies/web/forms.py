from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class EditUserForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', ]
