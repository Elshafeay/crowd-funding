from time import sleep

from factories.project import *
from factories.user import UserFactory


def run(n):
    try:
        n = int(n)
        print('Populating data...')
    except ValueError:
        print('Error: The parameter must be a number!')
        return

    sleep(1)
    print(f'=> Populating {n} users data...')
    UserFactory.create_batch(n)

    sleep(1)
    print(f'=> Populating categories data...')
    CategoryFactory.create_batch(8)

    sleep(1)
    print(f'=> Populating {n} projects data...')
    ProjectFactory.create_batch(n)

    sleep(1)
    print(f'=> Populating tags data...')
    TagFactory.create_batch(15)

    sleep(1)
    print(f'=> Populating {n*5} Project Tags...')
    print(f'Handling duplicates...')
    ProjectTagsFactory.create_batch(n*5)

    sleep(1)
    print(f'=> Populating {n*5} Saved Projects...')
    print(f'Handling duplicates...')
    SavedProjectsFactory.create_batch(n*5)

    sleep(1)
    print(f'=> Populating {n*5} Donations...')
    DonationFactory.create_batch(n*5)

    sleep(1)
    print(f'=> Populating {n*5} Reviews...')
    print(f'Handling duplicates...')
    ReviewFactory.create_batch(n*5)

    sleep(1)
    print(f'=> Populating {n*5} Comments...')
    CommentFactory.create_batch(n*5)

    sleep(1)
    print(f'=> Populating {n*5} Replies...')
    ReplyFactory.create_batch(n*5)

    sleep(1)
    print(f'=> Populating {n} Featured Projects...')
    FeaturedProjectsFactory.create_batch(n)
