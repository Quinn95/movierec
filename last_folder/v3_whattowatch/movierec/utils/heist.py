import guidebox
import json
from movierec.models import Movie, Genre, Person, Language, Keyword
import tmdbsimple as tmdb
import logging

guidebox.api_key = "26ba3cbb31750bcd51dede8068cf8ff72fcfde79"
guidebox.Region = "US"
tmdb.API_KEY = "f2eee9cde7536b5ef17767e4e9a97239"
logging.basicConfig(filename='heist.log',level=logging.DEBUG)


def test():
    # getNetflixMovies()
    # getAmazonMovies()
    # getHuluMovies()
    # createGenres()
    # populateMovieDetails()
    #getStreamingLinks(identifier=128834)
    #getManualLinks()
    pass


def getNetflixMovies():
    """
    Get a list of Netflix movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    netflix_movie_count = 250
    movie_offset = 0
    added_count = 0
    while netflix_movie_count > 0:
        #movies = guidebox.Movie.list(offset=movie_offset, limit=250, source='netflix')
        movies = guidebox.Movie.list(offset=movie_offset, limit=10, sources='netflix')
        list = json.loads(movies.__str__())
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
                added_count += 1
            else:
                obj = Movie.objects.get(identifier=int(result['id']))
                obj.netflix_available = True
                obj.save()
    logging.debug('Added ' + added_count.__str__() + ' new movies to the database from NetFlix')



def getAmazonMovies():
    """
    Get a list of Amazon Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    amazon_movie_count = 250
    movie_offset = 0
    added_count = 0
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
                added_count += 1
            else:
                obj = Movie.objects.get(identifier=int(result['id']))
                obj.amazon_available = True
                obj.save()
    logging.debug('Added ' + added_count.__str__() + ' new movies to the database from Amazon Prime')


def getHuluMovies():
    """
    Get a list of Hulu Plus movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    hulu_movie_count = 250
    movie_offset = 0
    added_count = 0
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
                added_count += 1
            else:
                obj = Movie.objects.get(identifier=int(result['id']))
                obj.hulu_available = True
                obj.save()
    logging.debug('Added ' + added_count.__str__() + ' new movies to the database from Hulu Plus')


def populateMovieDetails():
    """
    Gets details for all movies in the database using the TMDb API and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_set = Movie.objects.filter()
    logging.info('There are currently ' + len(movie_set).__str__() + ' total movies in the database')
    movie_retrieve_count = 0
    for movie in movie_set:
        if (not movie.tmdb_get) and (movie.themoviedb is not None):
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
            movie_retrieve_count += 1
        else:
            logging.debug('Either ' + movie.title + ' already has movie details retrieved or no TMDb id exists')
    logging.debug('Details for ' + movie_retrieve_count.__str__() + ' movies retrieved successfully')



def createGenres():
    """
    Should be called only once!!!
    Creates all genres for movies using the TMDb API

    Args:
        None
    Returns:
        None
    """
    genres = tmdb.Genres().list()

    genre_count = 0
    for genre in genres['genres']:
        if len(Genre.objects.filter(identifier=int(genre['id']))) == 0:
            g = Genre(identifier=int(genre['id']), name=genre['name'])
            g.save()
            genre_count += 1
    logging.debug('Genres added to database: ' + genre_count.__str__())


def getStreamingLinks(identifier):
    """
    Gets links for streaming services from GuideBox API for a specific
    movie identifier and updates the movie entry in the database.

    Args:
        identifier: movie identifier, i.e. the GuideBox movie id
    Returns:
        None
    """
    if identifier is not None and type(identifier) == int:
        movie_id = int(identifier)
        detail = guidebox.Movie.retrieve(movie_id)
        movie = Movie.objects.get(identifier=movie_id)

        hulu_link = None
        netflix_link = None
        amazon_link = None

        for each in detail['subscription_web_sources']:
            if each['source'] == 'hulu_plus':
                hulu_link = each['link']
            elif each['source'] == 'netflix':
                netflix_link = each['link']
            elif each['source'] == 'shudder_amazon_prime':
                amazon_link = each['link']

        movie.hulu=hulu_link
        movie.netflix=netflix_link
        movie.amazon=amazon_link
        movie.save()
        logging.info('Links to subscription services added for ' + movie.title.__str__())
    else:
        logging.warning('No movie identifier was passed or the movie identifier is not an integer')


def getAllLinks():
    movie_set = Movie.objects.all();

    for movie in movie_set:
        print 'Getting links for: ' + movie.__str__()
        movie_detail = guidebox.Movie.retrieve(id=movie.identifier)
        detail = json.loads(movie_detail.__str__())

        hulu_link = None
        netflix_link = None
        amazon_link = None

        for each in detail['subscription_web_sources']:
            if each['source'] == 'hulu_plus':
                hulu_link = each['link']
            elif each['source'] == 'netflix':
                netflix_link = each['link']
            elif each['source'] == 'shudder_amazon_prime':
                amazon_link = each['link']

        movie.hulu = hulu_link
        movie.netflix = netflix_link
        movie.amazon = amazon_link

        movie.save()

        logging.info('Links to subscription services added for ' + movie.title.__str__())


def getManualLinks():
    with open("link.txt", "r") as file:
        for line in file:
            array = line.split(" ")
            id = int(array[0])
            amazon_link = array[1]
            m = Movie.objects.filter(identifier=id)[:1]
            if len(m) != 0:
                movie = m[0]
                if len(amazon_link) == 0:
                    movie.amazon_available = False
                else:
                    movie.amazon = amazon_link
                movie.save()

