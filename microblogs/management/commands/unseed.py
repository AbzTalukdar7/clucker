from microblogs import models
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for item in models.User.objects.all():
            if item.is_superuser == False:
                item.delete()
        print("DONE")
