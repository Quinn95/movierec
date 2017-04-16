import guidebox
import gbox
from ..models import *
from django.db import models


def processRequest(request):
    #results = Movie.objects.filter(title__contains=request['title'])
    results = Movie.objects.all()

    for stream in request['streaming_services']:
        if stream == u'netflix':
            results = results.exclude(netflix__isnull=True)
        elif stream == u'amazon':
            results = results.exclude(amazon__isnull=True)
        elif stream == u'hulu':
            results = results.exclude(hulu__isnull=True)

    return results
