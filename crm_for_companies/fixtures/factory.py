import random
from datetime import datetime
import factory
from factory.faker import faker

from django.contrib.auth import get_user_model
from crm_for_companies.api_companies.models import Company
from crm_for_companies.api_employees.models import Employee

FAKE = faker.Faker()

UserModel = get_user_model()


# =================================================================
# Following rows should be executed one by one in Django console:
# =================================================================
# 1. python mange.py shell
# 2. from crm_for_companies.fixtures.factory import *
# 3. UsersFactory.create_batch(10)
# 4. following rows:
#       for c in range(5):
#           CompanyFactory.create(owner=random.choices(UserModel.objects.all(), k=3))
# # In above row k describes amount of owners per company
# 5. EmployeeFactory.create_batch(30)
# =================================================================


class UsersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserModel
        exclude = ('password',)

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    password = factory.PostGenerationMethodCall('set_password', '12345')
    #   In populations scripts we use 'make_password' in factory boy object is already created, so we use 'set_password'


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Faker("company")
    description = factory.Faker('sentence', nb_words=2)

    @factory.post_generation
    def owner(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, do nothing.
            return
        else:
            # Add the iterable of groups using bulk addition
            self.owner.add(*extracted)


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    date_of_birth = factory.Faker("date_between_dates",
                                  date_start=datetime(1955, 1, 1),
                                  date_end=datetime(2001, 12, 31))
    position = factory.Faker("job")
    salary = factory.Faker("randomize_nb_elements", number=1000, ge=True, max=10000)
    company = factory.Iterator(Company.objects.all())
