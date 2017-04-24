import guidebox
import json

guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"


def getSimilarMovies(identifier):
    try:
        similar = guidebox.Movie.related(id=identifier, sources='netflix, amazon_prime, hulu_plus')
    except:
        pass

    if similar == None:
        return None
    else:
        list = json.loads(similar.__str__())

        return_list = []

        for movie in list['results']:
            if (movie['themoviedb'] == 0 or movie['imdb'] == None):
                continue

            return_list.append(movie['id'])

        return return_list

