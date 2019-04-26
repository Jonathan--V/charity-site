from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from main.models.main.contact import Contact


class Command(BaseCommand):
    help = 'Performs the Django-specific set up steps for page testing'

    def handle(self, *args, **options):
        print(f'Django test setup started at {datetime.now()}')
        Contact.objects.create(
            area_of_responsibility="Head of Communications",
            title="Ms",
            first_name="Chats",
            last_name="Daily",
            email_address="Chats.Daily@example.com",
            publicly_viewable=True,
        )
        User.objects.create_superuser(
            username="test_admin",
            password="test_password1",
            email="test.admin@example.com",
        )
        print('Django test setup successful.')
