# Generated by Django 4.1.7 on 2023-07-14 15:14

import cloudinary.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import crm_for_companies.core.employees_functions


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("api_companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=300,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=300,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateField(
                        validators=[
                            crm_for_companies.core.employees_functions.validate_age
                        ]
                    ),
                ),
                (
                    "photo",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, verbose_name="image"
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        max_length=300,
                        validators=[django.core.validators.MinLengthValidator(2)],
                        verbose_name="Position in the company",
                    ),
                ),
                ("salary", models.IntegerField()),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="api_companies.company",
                    ),
                ),
            ],
        ),
    ]
