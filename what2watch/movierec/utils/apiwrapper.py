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
            results = filterStreamingServices(results, request[k])
        elif k == 'title':
            results = results.filter(title__contains=request[k])
        elif k == 'people':
            for person in request[k].split(','):
                print person
    return results

def filterStreamingServices(queryset, services):
    resultsn = Movie.objects.none()
    resultsa = Movie.objects.none()
    resultsh = Movie.objects.none()
    if len(services) != 0:
        for stream in services:
            if stream == u'netflix':
                resultsn = queryset.exclude(netflix_available=False)
            elif stream == u'amazon':
                resultsa = queryset.exclude(amazon_available=False)
            elif stream == u'hulu':
                resultsh = queryset.exclude(hulu_available=False)
        queryset = resultsn | resultsa | resultsh
    return queryset

