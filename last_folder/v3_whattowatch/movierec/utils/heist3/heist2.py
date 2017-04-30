import guidebox
import json

guidebox.api_key = 'd3c0fd429d3d77cce364497b2b4d5fc3f8d5c0f9'
guidebox.Region = 'US'


def getNetflixMovies():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    added_count = 0
    fo = open("netflix_idlist.txt", "a")
    while movie_count > 0:
        print 'Netflix: ' + str(movie_offset)
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='netflix')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        for result in movie_list['results']:
            if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
                continue

            id = result['id']
            fo.write(str(id) + '\n')
    fo.close()
    print "Done"


def getHuluMovies():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    added_count = 0
    fo = open("hulu_idlist.txt", "a")
    while movie_count > 0:
        print 'Hulu Plus:' + str(movie_offset)
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='hulu_plus')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        for result in movie_list['results']:
            if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
                continue

            id = result['id']
            fo.write(str(id) + '\n')
    fo.close()
    print "Done"


def getHBOMovies():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    added_count = 0
    fo = open("hbo_idlist.txt", "a")
    while movie_count > 0:
        print 'HBO Now' + str(movie_offset)
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='hbo_now')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        for result in movie_list['results']:
            if result['themoviedb'] == 0 or result['imdb'] is None or result['poster_400x570'] == 'http://static-api.guidebox.com/misc/default_movie_400x570.jpg':
                continue

            id = result['id']
            fo.write(str(id) + '\n')
    fo.close()
    print "Done"


#getHBOMovies()
