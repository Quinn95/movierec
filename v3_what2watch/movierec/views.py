from django.shortcuts import render
from django.http import HttpResponse

from utils import gbox, heist
from utils import apiwrapper
from .models import Person


from .models import Movie, Genre, Person, Keyword

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'movierec/home.html', {'user': user, 'movies' : None})

def test(request):
    heist.test()
    return HttpResponse("You got movies")

def recView(request):
    if request.method == 'POST':
        timerange = (request.POST['from'], request.POST['to'])

        genre = request.POST['genre']
        imdb = request.POST['imdb']
        #request.POST['mood']
        maxrating = request.POST['rating']
        keywords = request.POST.getlist('keywords')

        query = Movie.objects.all()
        if "people" in request.POST:
            people = request.POST.getlist('people')
        if timerange[0] != "-----": #we need to change
            query = query.filter(date__gt=int(timerange[0]))
        if timerange[1] != "-----": #we need to change
            query = query.filter(date__lte=int(timerange[1]))
        if genre != "Horror":
            genreQ = Genre.objects.get(name=genre)
            query = query.filter(genre__in=[genreQ])
        querynetflix = Movie.objects.none()
        queryamazon = Movie.objects.none()
        queryhulu = Movie.objects.none()
        anychecked = False;
        if "netflix" in request.POST:
            querynetflix = query.filter(netflix_available=True)
            anychecked = True
        if "amazon" in request.POST:
            queryamazon = query.filter(amazon_available=True)
            anychecked = True
        if "hulu" in request.POST:
            queryhulu = query.filter(hulu_available=True)
            anychecked = True

        if anychecked:
            query = querynetflix | queryamazon | queryhulu

        results = query

        print people

        return render(request, 'movierec/recpage.html',
                      {'results': results,
                       'user': request.user,
                       'people': Person.objects.all()})

    return render(request, 'movierec/recpage.html', {'user': request.user,
                           'people': Person.objects.all()})

