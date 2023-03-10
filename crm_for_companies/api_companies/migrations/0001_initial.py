# Generated by Django 4.1.7 on 2023-02-21 08:36

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('description', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(10)])),
                ('logo', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
            ],
        ),
    ]
