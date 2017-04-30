from django.core.management.base import BaseCommand
from optparse import make_option
from movierec.utils import heist

class Command(BaseCommand):
    help = "generates movies"

    def handle(self, **options):
        heist.createGenres()
        heist.populateMovieDetails()

