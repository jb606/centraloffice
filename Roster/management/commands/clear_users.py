from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):
    help = 'Remove dummy users.'
    def handle(self, *args, **options):
        users = User.objects.exclude(username='admin').delete()
        

