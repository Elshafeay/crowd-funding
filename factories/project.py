import random
import factory
from faker import Faker
from projects.models import *

faker = Faker()
users_lists = UserModel.objects.all()
projects_list = Project.objects.all()


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Iterator(
        [
            'Health', 'Sports', 'Food', 'Family',
            'Shelters', 'Poverty', 'Animals', 'Education'
        ]
    )

    class Meta:
        model = Category
        django_get_or_create = ('name',)


class ProjectFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: f'project-{n+1}')
    details = factory.Sequence(lambda n: f'{faker.text()}')
    target = factory.Sequence(lambda n: faker.random_int(min=100))
    start_date = factory.Sequence(
        lambda n: f'{faker.date_between(start_date="-3y", end_date="+1y")}')
    end_date = factory.Sequence(
        lambda n: f'{faker.date_between(start_date="+1y", end_date="+3y")}')
    category = factory.Sequence(lambda n: random.choice(Category.objects.all()))
    owner = factory.Sequence(lambda n: random.choice(users_lists))

    class Meta:
        model = Project


class TagFactory(factory.django.DjangoModelFactory):
    name = factory.Iterator(
        [
            'volleyball', 'basketball', 'football', 'tennis', 'swimming',
            'children', 'fathers', 'cats', 'dogs', 'money', 'schools',
            'universities', 'hospitals', 'refegees', 'investment'
        ]
    )

    class Meta:
        model = Tag
        django_get_or_create = ('name',)


class ProjectTagsFactory(factory.django.DjangoModelFactory):
    project = factory.Sequence(lambda n: random.choice(projects_list))
    tag = factory.Sequence(lambda n: random.choice(Tag.objects.all()))

    class Meta:
        model = ProjectTags
        django_get_or_create = ('project', 'tag',)


class SavedProjectsFactory(factory.django.DjangoModelFactory):
    project = factory.Sequence(lambda n: random.choice(projects_list))
    user = factory.Sequence(lambda n: random.choice(users_lists))

    class Meta:
        model = SavedProject
        django_get_or_create = ('project', 'user',)


class DonationFactory(factory.django.DjangoModelFactory):
    project = factory.Sequence(lambda n: random.choice(projects_list))
    user = factory.Sequence(lambda n: random.choice(users_lists))
    donation = factory.Sequence(lambda n: faker.random_int(min=100, max=500))

    class Meta:
        model = Donation


class ReviewFactory(factory.django.DjangoModelFactory):
    project = factory.Sequence(lambda n: random.choice(projects_list))
    user = factory.Sequence(lambda n: random.choice(users_lists))
    rate = factory.Sequence(lambda n: faker.random_int(min=1, max=5))
    liked = factory.sequence(lambda n: faker.pybool())

    class Meta:
        model = Review
        django_get_or_create = ('project', 'user',)


class CommentFactory(factory.django.DjangoModelFactory):
    project = factory.Sequence(lambda n: random.choice(projects_list))
    user = factory.Sequence(lambda n: random.choice(users_lists))
    comment = factory.Sequence(lambda n: f'{faker.text()}')

    class Meta:
        model = Comment


class ReplyFactory(factory.django.DjangoModelFactory):
    comment = factory.Sequence(lambda n: random.choice(Comment.objects.all()))
    user = factory.Sequence(lambda n: random.choice(users_lists))
    reply = factory.Sequence(lambda n: f'{faker.text()}')

    class Meta:
        model = Reply


class FeaturedProjectsFactory(factory.django.DjangoModelFactory):
    project = factory.Sequence(lambda n: random.choice(projects_list))

    class Meta:
        model = FeaturedProject
        django_get_or_create = ('project',)
