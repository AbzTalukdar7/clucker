from microblogs import models
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import random

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        args = 1
        Faker.seed(args)

        for i in range (args):
            tempFname = self.faker.first_name()
            tempLname = self.faker.last_name()
            self.user = models.User.objects.create_user(
                username = f'@{tempFname}{tempLname}',
                first_name = tempFname,
                last_name = tempLname,
                email = f'{tempFname}{tempLname}@outlook.com',
                password = f'{tempFname}{tempLname}{random.randint(0,999)}',
                bio = f'{self.faker.paragraph()}'
            )
            self.user.full_clean()
            self.user.save()
        print("DONE")
