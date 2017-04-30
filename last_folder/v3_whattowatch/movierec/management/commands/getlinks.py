from django.core.management.base import BaseCommand
from optparse import make_option
from movierec.utils.heist2 import builddatabase

class Command(BaseCommand):
    help = "generates movies"

    def handle(self, **options):
        builddatabase.getManualLinks()

