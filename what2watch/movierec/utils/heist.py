import guidebox
import json
from movierec.models import Movie, Genre, Person, Language, Keyword
import tmdbsimple as tmdb

guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"
tmdb.API_KEY = "f2eee9cde7536b5ef17767e4e9a97239"


def test():
    getNetflixMovies()
    getAmazonMovies()
    getHuluMovies()
    createGenres()
    populateMovieDetails()

# This function populates the database with NetFlix movies
def getNetflixMovies():
    netflix_movie_count = 250
    movie_offset = 0
    while netflix_movie_count > 0:
        #movies = guidebox.Movie.list(offset=movie_offset, limit=250, source='netflix')
        movies = guidebox.Movie.list(offset=movie_offset, limit=10, sources='netflix')
        list = json.loads(movies.__str__())
        print list
        movie_offset += 250
        #netflix_movie_count = list['total_results'] - movie_offset
        netflix_movie_count -= movie_offset
        for result in list['results']:
            e = Movie.objects.filter(identifier=int(result['id']))

            #Only do this if movie does not exist in the database
            if len(e) == 0:
                m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          netflix_available=True)
                m.save()
            else:
                obj = Movie.objects.get(identifier=int(result['id']))
                obj.netflix_available = True
                obj.save()


# This function populates the database with Amazon movies
def getAmazonMovies():
    amazon_movie_count = 250
    movie_offset = 0
    while amazon_movie_count > 0:
        #movies = guidebox.Movie.list(offset=movie_offset, limit=250, source='amazon_prime')
        movies = guidebox.Movie.list(offset=movie_offset, limit=10, sources='amazon_prime')
        list = json.loads(movies.__str__())
        movie_offset += 250
        #amazon_movie_count = list['total_results'] - movie_offset
        amazon_movie_count -= movie_offset
        for result in list['results']:
            e = Movie.objects.filter(identifier=int(result['id']))

            # Only do this if movie does not exist in the database
            if len(e) == 0:
                m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          amazon_available=True)
                m.save()
            else:
                obj = Movie.objects.get(identifier=int(result['id']))
                obj.amazon_available = True
                obj.save()


# This function populates the database with Hulu movies
def getHuluMovies():
    hulu_movie_count = 250
    movie_offset = 0
    while hulu_movie_count > 0:
        #movies = guidebox.Movie.list(offset=movie_offset, limit=250, source='hulu_plus')
        movies = guidebox.Movie.list(offset=movie_offset, limit=10, sources='hulu_plus')
        list = json.loads(movies.__str__())
        movie_offset += 250
        #hulu_movie_count = list['total_results'] - movie_offset
        hulu_movie_count -= movie_offset
        for result in list['results']:
            e = Movie.objects.filter(identifier=int(result['id']))

            # Only do this if movie does not exist in the database
            if len(e) == 0:
                m = Movie(identifier=result['id'],
                          themoviedb=result['themoviedb'],
                          imdb=result['imdb'],
                          rating=result['rating'],
                          rottentomatoes=result['rottentomatoes'],
                          metacritic=result['metacritic'],
                          common_sense_media=result['common_sense_media'],
                          poster=result['poster_400x570'],
                          title=result['title'],
                          date=result['release_year'],
                          hulu_available=True)
                m.save()
            else:
                obj = Movie.objects.get(identifier=int(result['id']))
                obj.hulu_available = True
                obj.save()


# This function uses the TMDb api to retrieve movie details
def populateMovieDetails():
    movie_set = Movie.objects.filter()
    for movie in movie_set:
        if not movie.tmdb_get:
            tmdb_data = tmdb.Movies(movie.themoviedb).info(append_to_response='credits,videos,keywords')

            genre_list = []
            for genre in tmdb_data['genres']:
                genre_list.append(Genre.objects.get(identifier=genre['id']))

            keywords_list = []
            for keyword in tmdb_data['keywords']['keywords']:
                if len(Keyword.objects.filter(name=keyword['name'])) == 0:
                    k = Keyword(name=keyword['name'])
                    keywords_list.append(k)
                    k.save()
                else:
                    keywords_list.append(Keyword.objects.get(name=keyword['name']))

            people_list = []

            people = tmdb_data['credits']
            for cast in people['cast']:
                if len(Person.objects.filter(identifier=int(cast['id']))) == 0:
                    p = Person(identifier=int(cast['id']), name=cast['name'])
                    people_list.append(p)
                    p.save()
                else:
                    people_list.append(Person.objects.get(name=cast['name']))

            for crew in people['crew']:
                if crew['job'] == 'Director' or crew['job'] == 'Writer':
                    if len(Person.objects.filter(identifier=int(crew['id']))) == 0:
                        p = Person(identifier=int(crew['id']), name=crew['name'])
                        people_list.append(p)
                        p.save()
                    else:
                        people_list.append(Person.objects.get(name=crew['name']))

            language_list = []
            for language in tmdb_data['spoken_languages']:
                if len(Language.objects.filter(name=language['iso_639_1'])) == 0:
                    l = Language(name=language['iso_639_1'])
                    language_list.append(l)
                    l.save()
                else:
                    language_list.append(Language.objects.filter(name=language['iso_639_1'])[0])

            movie.genre.add(*genre_list)
            movie.people.add(*people_list)
            movie.keywords.add(*keywords_list)
            movie.languages.add(*language_list)
            movie.summary=tmdb_data['overview']
            movie.runtime=tmdb_data['runtime']
            movie.budget=tmdb_data['budget']
            movie.vote_count=tmdb_data['vote_count']
            movie.vote_average=tmdb_data['vote_average']
            movie.popularity=tmdb_data['popularity']
            movie.trailer='https://www.youtube.com/embed/'+tmdb_data['videos']['results'][0]['key']
            movie.tmdb_get=True
            movie.save()



def createGenres():
    genres = tmdb.Genres().list()

    for genre in genres['genres']:
        if len(Genre.objects.filter(identifier=int(genre['id']))) == 0:
            g = Genre(identifier=int(genre['id']), name=genre['name'])
            g.save()