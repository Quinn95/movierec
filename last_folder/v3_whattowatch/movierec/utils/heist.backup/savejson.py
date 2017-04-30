import guidebox
import json

guidebox.api_key = 'd3c0fd429d3d77cce364497b2b4d5fc3f8d5c0f9'
guidebox.Region = 'US'

def getNetflixMoviesJSON():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    i = 0
    while movie_count > 0:
        fo = open("netflix/netflix_" + str(i) + ".json", "a")
        print 'Netflix: ' + str(i)
        i += 1
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='netflix')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        fo.write(str(movies) + '\n')
        fo.close()
    print "Done"


def getAmazonMoviesJSON():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    i = 0
    while movie_count > 0:
        fo = open("amazon/amazon_" + str(i) + ".json", "a")
        print 'Amazon Prime: ' + str(i)
        i += 1
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='amazon_prime')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        fo.write(str(movies) + '\n')
        fo.close()
    print "Done"

def getHuluMoviesJSON():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    i = 0
    while movie_count > 0:
        fo = open("hulu/hulu_" + str(i) + ".json", "a")
        print 'Hulu Plus: ' + str(i)
        i += 1
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='hulu_plus')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        fo.write(str(movies) + '\n')
        fo.close()
    print "Done"


def getHBOMoviesJSON():
    """
    Get a list of Netflix Prime movies from GuideBox and populates the database

    Args:
        None
    Returns:
        None
    """
    movie_count = 250
    movie_offset = 0
    i = 0
    while movie_count > 0:
        fo = open("hbo/hbo_" + str(i) + ".json", "a")
        print 'HBO Now: ' + str(i)
        i += 1
        movies = guidebox.Movie.list(offset=movie_offset, limit=250, sources='hbo_now')
        movie_list = json.loads(movies.__str__())
        movie_offset += 250
        movie_count = movie_list['total_results'] - movie_offset
        fo.write(str(movies) + '\n')
        fo.close()
    print "Done"


#getHuluMoviesJSON()
