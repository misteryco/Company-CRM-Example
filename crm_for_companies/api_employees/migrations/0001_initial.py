# Generated by Django 4.1.7 on 2023-02-21 11:47

import cloudinary.models
import crm_for_companies.api_employees.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_companies', '0002_alter_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('date_of_birth', models.DateField(verbose_name=crm_for_companies.api_employees.models.validate_age)),
                ('photo', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('position', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Position in the company')),
                ('salary', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api_companies.company')),
            ],
        ),
    ]
