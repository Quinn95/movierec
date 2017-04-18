import guidebox
import gbox
from ..models import *
from django.db import models


def processRequest(request):
    #results = Movie.objects.filter(title__contains=request['title'])
    results = Movie.objects.all()
    resultsn = Movie.objects.none()
    resultsa = Movie.objects.none()
    resultsh = Movie.objects.none()
    ###
    #   Bug... Filters work as logical and, not logical or for streaming
    #   services. Ie, if user checks netflix and amazon, it gets movies on
    #   netflix && amazon.
    ###
    for k, v in request.items():
        if k == 'streaming_services':
            for stream in v:
                if stream == u'netflix':
                    resultsn = results.exclude(netflix__isnull=True)
                elif stream == u'amazon':
                    resultsa = results.exclude(amazon__isnull=True)
                elif stream == u'hulu':
                    resultsh = results.exclude(hulu__isnull=True)
            if len(v) != 0:
                results = resultsn | resultsa | resultsh

        elif k == 'title':
            results = results.filter(title__contains=request[k])
        elif k == 'people':
            for person in request[k].split(','):
                print person

    return results
