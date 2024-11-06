from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates dummy users.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of users to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']

        for _ in range(count):
            username = fake.user_name()
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()

            User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} users.'))