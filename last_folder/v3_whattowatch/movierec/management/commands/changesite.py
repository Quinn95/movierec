from django.core.management.base import BaseCommand
from optparse import make_option
from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = "generates movies"

    def handle(self, **options):
        site = Site.objects.get_current()
        site.domain = 'w2w.com'
        site.name = 'WhatToWatch'
        site.save()