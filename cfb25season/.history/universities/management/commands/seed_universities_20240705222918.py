# universities/management/commands/seed_universities.py
from django.core.management.base import BaseCommand

from universities.models import University


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        universities = [
            {'name': 'University of Miami', 'latitude': 25.7174, 'longitude': -80.2785, 'logo_url': 'url_to_logo'},
            # Add all universities here...
        ]
        for uni in universities:
            University.objects.create(**uni)
