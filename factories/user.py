import os
from django.conf import settings
import factory
from faker import Faker
from users.models import UserModel

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: f'{faker.email()}')
    first_name = factory.Sequence(lambda n: f'{faker.first_name()}')
    last_name = factory.Sequence(lambda n: f'{faker.last_name()}')
    phone = factory.Sequence(lambda n: f'{faker.phone_number()[:10]}')
    password = 'password@123456'
    
    class Meta:
        model = 'users.UserModel'
