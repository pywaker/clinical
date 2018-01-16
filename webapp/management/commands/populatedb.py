
from django.core.management.base import BaseCommand, CommandError

from ._private import create_doctors, create_patients


class Command(BaseCommand):
    help = "populate entire database for testing and development"

    def handle(self, *args, **options):
        # print("hello world")
        create_doctors()
        create_patients()
