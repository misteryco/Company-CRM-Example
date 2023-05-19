from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class EditUserForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField}
