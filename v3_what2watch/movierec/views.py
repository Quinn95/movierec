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
        people = request.POST.getlist('people[]')
        keywords = request.POST.getlist('keywords')
        netflix = request.POST['netflix']
#        amazon = request.POST['amazon']
#        hulu = request.POST['hulu']

        query = Movie.objects.all()

        if timerange[0] != "2017":
            query = query.filter(date__gte=int(timerange[0]))
        if timerange[1] != "2017":
            query = query.filter(date__lte=int(timerange[1]))
        if genre != "Horror":
            genreQ = Genre.objects.get(name=genre)
            query = query.filter(genre__in=[genreQ])
        results = query

        print people

        return render(request, 'movierec/recpage.html',
                      {'results': results,
                       'user': request.user,
                       'people': Person.objects.all()})

    return render(request, 'movierec/recpage.html', {'user': request.user,
                           'people': Person.objects.all()})

