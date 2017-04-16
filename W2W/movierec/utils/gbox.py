import guidebox
import json
from movierec.models import Movie, Genre, Person
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
    #populateMovies(guidebox.Movie.list(limit=10))
    populateMovies(guidebox.Movie.list(limit=100))

def populateMovies(movies):

    list = json.loads(movies.__str__())

    for movie in list['results']:
        e = Movie.objects.filter(identifier=int(movie['id']))
        if len(e) == 0:
            hulu_link = None
            netflix_link = None
            amazon_link = None
            movie_detail = guidebox.Movie.retrieve(movie['id'])
            detail = json.loads(movie_detail.__str__())
            genre_list = []
            for genre in detail['genres']:
                if len(Genre.objects.filter(name=genre['title'])) == 0:
                    g = Genre(identifier=genre['id'], name=genre['title'])
                    genre_list.append(g)
                    g.save()

            person_list = []
            for actor in detail['cast']:
                if len(Person.objects.filter(name=actor['name'])) == 0:
                    p = Person(identifier=actor['id'], name=actor['name'])
                    person_list.append(p)
                    p.save()
            for director in detail['directors']:
                if len(Person.objects.filter(name=director['name'])) == 0:
                    d = Person(identifier=director['id'], name=director['name'])
                    person_list.append(d)
                    d.save()

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
            m.genre.add(*genre_list)
            m.people.add(*person_list)
            m.save()

