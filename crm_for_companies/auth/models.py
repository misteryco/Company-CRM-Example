from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models


class AppUser(auth_models.AbstractUser):
    pass
