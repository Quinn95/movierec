import guidebox
import json
from movierec.models import Movie

guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"

"""
m = Movie()
m.identifier = 1
m.themoviedb = "link"
m.save()
"""

def populateMovies(movies):
    list = json.loads(movies.__str__())

"""
"common_sense_media": "https://www.commonsensemedia.org/movie-reviews/sing",
      "freebase": "",
      "id": 143442,
      "imdb": "tt3470600",
      "in_theaters": true,
      "metacritic": "http://www.metacritic.com/movie/sing",
      "original_title": "Sing",
      "poster_120x171": "http://static-api.guidebox.com/091716/thumbnails_movies_small/143442-6406127447-9196517081-960917864-small-120x171.jpg",
      "poster_240x342": "http://static-api.guidebox.com/091716/thumbnails_movies_medium/143442-4780924805-2656850810-7933440194-medium-240x342.jpg",
      "poster_400x570": "http://static-api.guidebox.com/091716/thumbnails_movies/-143442-9534959495-9127518967-101791034-large-400x570.jpg",
      "pre_order": false,
      "rating": "PG",
      "release_date": "2016-12-08",
      "release_year": 2016,
      "rottentomatoes": 771434221,
      "themoviedb": 335797,
      "title": "Sing",
      "wikipedia_id": 47415762
"""

"""
    identifier = models.IntegerField()
    themoviedb = models.IntegerField()
    imdb = models.IntegerField()
    rating = models.CharField(max_length=7)
    rottentomatoes = models.IntegerField()
    wikipedia_id = models.IntegerField()
    metacritice = models.CharField()
    common_sense_media = models.CharField()
    poster = models.CharField()
    title = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Person)
    directors = models.ManyToManyField(Person)
    date = models.DateField()
    language = models.CharField(max_length=2) #may change
"""
    for movie in list['results']:
        m = Movie(identifier=movie['id'],
                  themoviedb=movie['themoviedb'],
                  imdb=movie['imdb'],
                  rating=movie['rating'],
                  rottentomatoes=movie['rottentomatoes'],
                  wikipedia_id=movie['wikipedia_id'],
                  )

