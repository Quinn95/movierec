import json

class Movie(object):
    def __init__(self, title, id_number):
        self.title = title
        self.id = id_number

    def __str__(self):
        return self.title

"""
query database for parameters
query can be genre + actors for example
if query yeilds movies:
    load from database
else:
    json = api.movies.list()
    for movie in json:
        movie_object = jsonToMovie(movie)
        database.store(movie_object)

"""


def jsonToMovie(inString):
    decoded = json.loads(inString)
    movies = decoded['movies']

    movieclasslist = []
    print len(movies)
    for movie in movies:
        title = movie['title']
        id_number = movie['id']
        movieclasslist.append(Movie(title, id_number))
    return movieclasslist

def main():
    instring = '{"movies": [{"id": 0, "title": "tucker"}, {"id": 1, "title": "nemo"}]}'
    test = jsonToMovie(instring)

    print test

if __name__ == "__main__":
    main()

