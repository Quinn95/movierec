import guidebox
import json
from movierec.models import Movie
from django.db import models


guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"

"""
m = Movie()
m.identifier = 1
m.themoviedb = "link"
m.save()
"""
def testing():
    populateMovies(guidebox.Movie.list(limit=5))
    populateMovies(guidebox.Movie.list(limit=5))

def populateMovies(movies):

    list = json.loads(movies.__str__())

    for movie in list['results']:

        e = Movie.objects.filter(identifier=int(movie['id']))
        if len(e) == 0:
            movie_detail = guidebox.Movie.retrieve(movie['id'])
            detail = json.loads(movie_detail.__str__())
            for each in detail['subscription_web_sources']:
                if each['source'] == 'hulu_plus':
                    hulu_link = each['link']
                elif each['source'] == 'netflix':
                    netflix_link = each['link']
                elif each['source'] == 'shudder_amazon_prime':
                    amazon_link = each['link']

            m = Movie(identifier=movie['id'],
                      themoviedb=movie['themoviedb'],
                      imdb=movie['imdb'],
                      rating=movie['rating'],
                      rottentomatoes=movie['rottentomatoes'],
                      wikipedia_id=movie['wikipedia_id'],
                      metacritic=movie['metacritic'],
                      common_sense_media=movie['common_sense_media'],
                      poster=movie['poster_400x570'],
                      title=movie['title'],
                      date=movie['release_year'],
                      netflix=netflix_link,
                      amazon=amazon_link,
                      hulu=hulu_link)


            m.save()

