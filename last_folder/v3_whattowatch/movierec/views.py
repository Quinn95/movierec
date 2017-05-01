from django.shortcuts import render
from django.http import HttpResponse

from utils import gbox, heist
from utils import apiwrapper
from django.core.paginator import Paginator


from .models import Movie, Genre, Person, Keyword, Person, Language

from useraccount.models import UserProfile


# Create your views here.

def home(request):
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    
    query = Movie.objects.all()
    query = query.exclude(popularity__exact=None)
    query = query.exclude(date__exact=None)
    query = query.exclude(vote_average__exact=None)

    # Initialize site queries #
    querynetflix = Movie.objects.none()
    queryamazon = Movie.objects.none()
    queryhulu = Movie.objects.none()
    queryhbo = Movie.objects.none()
    anychecked = False

    if profile != None:
        # Check if any specific site is selected #
        if (profile.show_netflix == True):
            querynetflix = query.filter(netflix_available = True)
            anychecked = True
        if (profile.show_amazon == True):
            queryamazon = query.filter(amazon_available = True)
            anychecked = True
        if (profile.show_hulu == True):
            queryhulu = query.filter(hulu_available = True)
            anychecked = True
        if (profile.show_hbo == True):
            queryhbo = query.filter(hbo_available = True)
            anychecked = True

        # No specific sites selected #
        if anychecked: query = querynetflix | queryamazon | queryhulu | queryhbo
        query = query.distinct()
    
    trending = query.order_by('-popularity')[:30]

    recent = query.order_by('-date')[:30]

    random = query.order_by('?')[:30]

    vote_average = query.order_by('-vote_average')[:30]
        
    return render(request, 'movierec/home.html', 
                            {'profile': profile, 
                            'user': request.user, 
                            'trending': trending, 
                            'recent': recent, 
                            'random': random, 
                            'vote_average': vote_average})

def test(request):
    heist.test()
    return HttpResponse("You got movies")

# Defined user ratings #
USER_RATINGS = {"Any": [0.0, 10.0], "> 8": [8.0, 10.0], "6-8": [6.0, 8.0],
                "4-6": [4.0, 6.0], "< 4": [0.0, 4.0]}

def recView(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
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
        peoplelist = request.POST.getlist('people[]')
        if len(peoplelist) > 0:
            peoplequerylist = map(lambda x: Person.objects.filter(name__icontains = x).first(), peoplelist)
            query = query.filter(people__in = peoplequerylist)
        
        # Check if any keywords were inputted #
        keywords = request.POST.getlist('keywords[]')
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

        if (request.POST["netflix"] == "true"):
            querynetflix = query.filter(netflix_available = True)
            anychecked = True
        if (request.POST["amazon"] == "true"):
            queryamazon = query.filter(amazon_available = True)
            anychecked = True
        if (request.POST["hulu"] == "true"):
            queryhulu = query.filter(hulu_available = True)
            anychecked = True
        if (request.POST["hbo"] == "true"):
            queryhbo = query.filter(hbo_available = True)
            anychecked = True

        # No specific sites selected #
        if anychecked: 
            query = querynetflix | queryamazon | queryhulu

        # Display first 20 results #
        query = query.distinct()
        results = query[:70]

        # Return all items #
        return render(request, 'movierec/recpage.html',
                     {'results': results,
                      'profile': profile,
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

paginator = None;
def search(request):
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        if int(request.POST['pageNum']) == 1:
            search_query = request.POST['search_text']
            print search_query
            query = Movie.objects.all()

            if len(search_query) != 0:
                query = query.filter(title__icontains = search_query)

            # Initialize site queries #
            querynetflix = Movie.objects.none()
            queryamazon = Movie.objects.none()
            queryhulu = Movie.objects.none()
            queryhbo = Movie.objects.none()
            anychecked = False

            # Check if any specific site is selected #
            if (request.POST["netflix"] == "true"):
                querynetflix = query.filter(netflix_available = True)
                anychecked = True
            if (request.POST["amazon"] == "true"):
                queryamazon = query.filter(amazon_available = True)
                anychecked = True
            if (request.POST["hulu"] == "true"):
                queryhulu = query.filter(hulu_available = True)
                anychecked = True
            if (request.POST["hbo"] == "true"):
                queryhbo = query.filter(hbo_available = True)
                anychecked = True

            # No specific sites selected #
            if anychecked: query = querynetflix | queryamazon | queryhulu | queryhbo
            query = query.distinct()
            global paginator
            if len(query) >= 100:
                paginator = Paginator(list(query), 100)
            else:
                paginator = Paginator(list(query), 5)
            results = paginator.page(1)
        else:
            results = paginator.page(int(request.POST['pageNum']))

        return render(request, 'movierec/search.html', {'results': results,
                                                        'profile': profile,
                                                        'user': request.user})

    return render(request, 'movierec/search.html', {'profile': profile, 'user': request.user})


def like_dislike(request):
    # if request.method == 'POST':
    #     user = request.user
    #     if user.is_authenticated:
    #         #profile = Profile.objects.get(user=user) 
    #         movie = request.POST['movie']
    #         like_dislike = request.POST['like_dislike']
    #         if like_dislike == True:
    #             #profile.liked_movies.add(movie)
    #         elif like_dislike == False:
    #             #profile.disliked_movies.add(movie)
    #         #profile.save()
    return HttpResponse("/")


            #like = True
            #dislike = False

