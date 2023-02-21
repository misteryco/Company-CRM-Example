from django.core.validators import MinLengthValidator
from django.db import models


class Company(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 3
    DESCRIPTION_MIN_LENGTH = 10
    DESCRIPTION_MAX_LENGTH = 300

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
        ),
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(
            MinLengthValidator(DESCRIPTION_MIN_LENGTH),
        ),
        null=False,
        blank=False,

    )
    #
    # logo = models.ImageField(
    #
    # )
