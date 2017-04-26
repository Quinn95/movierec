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

MOODS = {"Happy": ["Animation","Comedy","Family","Romance"], 
         "Sad": ["Crime", "Documentary", "Drama", "History", "Horror","War"],
         "Angry": ["Action", "Adventure", "Crime", "Documentary", "Horror", 
                   "Thriller", "War"],
         "Pumped": ["Action", "Adventure:", "Crime", "Fantasy", "Horror",
                    "Science Fiction", "Thriller", "War", "Western"],
         "Evil": ["History", "Horror", "Thriller", "Crime", "War"]}

def recView(request):
    if request.method == 'POST':
        timerange = (request.POST['from'], request.POST['to'])

        genre = request.POST['genre']
        imdb = request.POST['imdb']
        maxrating = request.POST['rating']
        people = request.POST.getlist('people')
        mood = request.POST['mood']

        query = Movie.objects.all()

        if maxrating != "Any":
            query = query.filter(rating=maxrating)

        peoplelist = request.POST.getlist('people')
        if len(peoplelist) > 0:
            peoplequerylist = map(lambda x:
                             Person.objects.filter(name__icontains=x).first(),
                             people)
            query = query.filter(people__in=peoplequerylist)
        keywords = request.POST.getlist('keywords')
        if len(keywords) > 0:
            keylist = map(lambda x: Keyword.objects.get(name=x), keywords)
            query = query.filter(keywords__in=keylist)

        if timerange[0] != "-----": #we need to change
            query = query.filter(date__gte=int(timerange[0]))
        if timerange[1] != "-----": #we need to change
            query = query.filter(date__lte=int(timerange[1]))

       #if mood != "Any":

        if genre != "Any":
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

        results = query[:20]

        return render(request, 'movierec/recpage.html',
                      {'results': results,
                       'user': request.user,
                       'people': Person.objects.all(),
                      'genres': Genre.objects.all(),
                      'keywords': Keyword.objects.all()})

    return render(request, 'movierec/recpage.html', {'user': request.user,
                           'people': Person.objects.all(), 'genres': Genre.objects.all(),
                  'keywords': Keyword.objects.all()})

