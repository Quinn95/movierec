import guidebox
import json
from movierec.models import Movie, Genre, Person, Language
from django.db import models
import tmdbsimple as tmdb

guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"
tmdb.API_KEY = "f2eee9cde7536b5ef17767e4e9a97239"

"""
m = Movie()
m.identifier = 1
m.themoviedb = "link"
m.save()
"""
def testing():
    #populateMovies(guidebox.Movie.list(limit=10))
    populateMovies(guidebox.Movie.list(limit=10))
    # g = Genre.objects.get(name='Action')
    # print g.movie_set.all()


def populateMovies(movies):

    list = json.loads(movies.__str__())

    for movie in list['results']:
        e = Movie.objects.filter(identifier=int(movie['id']))
        tmdb_data = tmdb.Movies(movie['themoviedb']).info()
        if len(e) == 0:
            hulu_link = None
            netflix_link = None
            amazon_link = None
            movie_detail = guidebox.Movie.retrieve(movie['id'])
            detail = json.loads(movie_detail.__str__())
            genre_list = []
            for genre in detail['genres']:
                if len(Genre.objects.filter(identifier=int(genre['id']))) == 0:
                    g = Genre(identifier=int(genre['id']), name=genre['title'])
                    genre_list.append(g)
                    g.save()
                else:
                    genre_list.append(Genre.objects.filter(name=genre['title'])[0])

            person_list = []
            for actor in detail['cast']:
                if len(Person.objects.filter(identifier=int(actor['id']))) == 0:
                    p = Person(identifier=int(actor['id']), name=actor['name'])
                    person_list.append(p)
                    p.save()
                else:
                    person_list.append(Person.objects.filter(name=actor['name'])[0])
            for director in detail['directors']:
                if len(Person.objects.filter(identifier=int(director['id']))) == 0:
                    d = Person(identifier=int(director['id']), name=director['name'])
                    person_list.append(d)
                    d.save()
                else:
                    person_list.append(Person.objects.filter(name=director['name'])[0])
            for writer in detail['writers']:
                if len(Person.objects.filter(identifier=int(writer['id']))) == 0:
                    w = Person(identifier=int(writer['id']), name=writer['name'])
                    person_list.append(w)
                    w.save()
                else:
                    person_list.append(Person.objects.filter(name=writer['name'])[0])

            language_list = []
            for language in tmdb_data['spoken_languages']:
                if len(Language.objects.filter(name=language['iso_639_1'])) == 0:
                    l = Language(name=language['iso_639_1'])
                    language_list.append(l)
                    l.save()
                else:
                    language_list.append(Language.objects.filter(name=language['iso_639_1'])[0])

            main_trailer = detail['trailers']['web'][0]['embed']

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
                      summary=detail['overview'],
                      runtime=tmdb_data['runtime'],
                      budget=tmdb_data['budget'],
                      vote_count=tmdb_data['vote_count'],
                      vote_average=tmdb_data['vote_average'],
                      popularity=tmdb_data['popularity'],
                      date=movie['release_year'],
                      netflix=netflix_link,
                      amazon=amazon_link,
                      hulu=hulu_link,
                      trailer=main_trailer)
            m.save()
            m.genre.add(*genre_list)
            m.people.add(*person_list)
            m.languages.add(*language_list)
            m.save()

