from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from utils import gbox, heist
from utils import apiwrapper


from .models import Movie, Genre, Person, Keyword, Person, Language

from v3_whattowatch.models import UserProfile

from useraccount.models import Profile


# Create your views here.

def home(request):
    user = request.user
    return render(request, 'movierec/home.html', {'user': user, 'movies' : None})

def test(request):
    heist.test()
    return HttpResponse("You got movies")

# Defined user ratings #
USER_RATINGS = {"Any": [0.0, 10.0], "> 8": [8.0, 10.0], "6-8": [6.0, 8.0],
                "4-6": [4.0, 6.0], "< 4": [0.0, 4.0]}

def recView(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user),
    else:
        profile = None
    if request.method == 'POST':

        # Form name definitions #
        timerange = (request.POST['from'], request.POST['to'])
        genre = request.POST['genre']
        imdb = request.POST['imdb']
        mpaarating = request.POST['rating']
        people = request.POST.getlist('people')
        language = request.POST['language']
        query = Movie.objects.all()

        # Check if MPAA is selected #
        if mpaarating != "Any":
            query = query.filter(rating=mpaarating)

        # Check if IMDB rating is selected #
        if imdb != "Any":
            minrating, maxrating = USER_RATINGS[imdb]
            query = query.filter(vote_average__gte=minrating)
            query = query.filter(vote_average__lte=maxrating)

        # Check if any people were selected #
        peoplelist = request.POST.getlist('people')
        if len(peoplelist) > 0:
            peoplequerylist = map(lambda x: Person.objects.filter(name__icontains = x).first(), people)
            query = query.filter(people__in = peoplequerylist)
        
        # Check if any keywords were inputted #
        keywords = request.POST.getlist('keywords')
        if len(keywords) > 0:
            keylist = map(lambda x: Keyword.objects.get(name = x), keywords)
            query = query.filter(keywords__in = keylist)

        # Check against initial time range #
        if timerange[0] != "-----": #we need to change
            query = query.filter(date__gte = int(timerange[0]))
        if timerange[1] != "-----": #we need to change
            query = query.filter(date__lte = int(timerange[1]))

        # Check if any language is selected #
        if language != "Any":
            languageOb = Language.objects.get(name = language)
            query = query.filter(languages__in = [languageOb])

        # Check if any genre is selected #
        if genre != "Any":
            genreQ = Genre.objects.get(name = genre)
            query = query.filter(genre__in = [genreQ])

        # Initialize site queries #
        querynetflix = Movie.objects.none()
        queryamazon = Movie.objects.none()
        queryhulu = Movie.objects.none()
        anychecked = False

        # Check if any specific site is selected #
        if not (("netflix" in request.POST) and ("amazon" in request.POST) and 
                ("hulu" in request.POST)):
            if "netflix" in request.POST:
                querynetflix = query.filter(netflix_available = True)
                anychecked = True
            if "amazon" in request.POST:
                queryamazon = query.filter(amazon_available = True)
                anychecked = True
            if "hulu" in request.POST:
                queryhulu = query.filter(hulu_available = True)
                anychecked = True

        # No specific sites selected #
        if anychecked: query = querynetflix | queryamazon | queryhulu

        # Display first 20 results #
        query = query.distinct()
        results = query[:70]

        # Return all items #
        return render(request, 'movierec/recpage.html',
                     {'results': results,
                      'user': request.user,
                      'people': Person.objects.all(),
                      'genres': Genre.objects.all(),
                      'keywords': Keyword.objects.all()})

    # Return all items #
    return render(request, 'movierec/recpage.html',
                 {'user': request.user,
                  'profile': profile, 
                  'people': Person.objects.all(),
                  'genres': Genre.objects.all(),
                  'keywords': Keyword.objects.all()})

def search(request):
    if request.method == 'POST':
        search_query = request.POST['search_text']
        query = Movie.objects.all()

        if len(search_query) != 0:
            query = query.filter(title__icontains = search_query)

        # Initialize site queries #
        querynetflix = Movie.objects.none()
        queryamazon = Movie.objects.none()
        queryhulu = Movie.objects.none()
        anychecked = False

        # Check if any specific site is selected #
        if not (("netflix" in request.POST) and ("amazon" in request.POST) and 
                ("hulu" in request.POST)):
            if "netflix" in request.POST:
                querynetflix = query.filter(netflix_available = True)
                anychecked = True
            if "amazon" in request.POST:
                queryamazon = query.filter(amazon_available = True)
                anychecked = True
            if "hulu" in request.POST:
                queryhulu = query.filter(hulu_available = True)
                anychecked = True

        # No specific sites selected #
        if anychecked: query = querynetflix | queryamazon | queryhulu
        
        query = query.distinct()
        results = query[:100]

        return render(request, 'movierec/search.html', {'results': results})
        
    return render(request, 'movierec/search.html')


def like_dislike(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            profile = Profile.objects.get(user=user) 
            movie = request.POST['movie']
            like_dislike = request.POST['like_dislike']
            if like_dislike == True:
                profile.liked_movies.add(movie)
            elif like_dislike == False:
                profile.disliked_movies.add(movie)
            profile.save()
    return HttpResponse("/")


            #like = True
            #dislike = False
