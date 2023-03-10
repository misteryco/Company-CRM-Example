from datetime import date, timedelta

from django.core.validators import MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError

from cloudinary import models as cloudinary_models

from crm_for_companies.api_companies.models import Company


def validate_age(value):
    min_age_employee = 16
    delta_age = date.today().year - value.year
    if delta_age <= min_age_employee:
        raise ValidationError(f'Employee should be at least {min_age_employee} years old')


class Employee(models.Model):
    NAME_MAX_LEN = 50
    NAME_MIN_LEN = 2
    DESCRIPTION_MIN_LENGTH = 10
    DESCRIPTION_MAX_LENGTH = 300
    POSITION_MAX_LEN = 50
    POSITION_MIN_LEN = 2

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            MinLengthValidator(NAME_MIN_LEN),
        ),
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        validators=(
            validate_age,
        ),
    )

    photo = cloudinary_models.CloudinaryField(
        'image',
        null=False,
        blank=True,

    )

    position = models.CharField(
        max_length=POSITION_MAX_LEN,
        validators=(MinLengthValidator(POSITION_MIN_LEN),
                    ),
        null=False,
        blank=False,
        verbose_name='Position in the company',
    )

    salary = models.IntegerField(
        null=False,
        blank=False,
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}, works at: {self.company}.'
