import guidebox
import gbox
from ..models import *
from django.db import models


def processRequest(request):
    #results = Movie.objects.filter(title__contains=request['title'])
    results = Movie.objects.all()

    ###
    #   Bug... Filters work as logical and, not logical or for streaming
    #   services. Ie, if user checks netflix and amazon, it gets movies on
    #   netflix && amazon.
    ###
    for k, v in request.items():
        if k == 'streaming_services':
            for stream in request[k]:
                if stream == u'netflix':
                    results = results.exclude(netflix__isnull=True)
                elif stream == u'amazon':
                    results = results.exclude(amazon__isnull=True)
                elif stream == u'hulu':
                    results = results.exclude(hulu__isnull=True)
        elif k == 'title':
            results = results.filter(title__contains=request[k])
        elif k == 'people':
            for person in request[k].split(','):
                print person

    return results
