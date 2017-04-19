import guidebox
import json

# from tmdbv3api import TMDb
#
# tmdb = TMDb(api_key="f2eee9cde7536b5ef17767e4e9a97239", debug=False, lang="en")
#
# popular = tmdb.search("Tucker and Dale")
#
#
# movie = tmdb.get_movie(343611)
# print movie.title
# print movie.overview
# print movie.popularity
# print movie.poster_path
# print movie.amazon_link
#

#key : e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5
guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"

# movies = guidebox.Movie.list(limit=100)
#
# list = json.loads(movies.__str__())
#
# for movie in list['results']:
#     m = Movie(title=movie['title'], identifier=movie['id'], imdb=movie['imdb'], )
#     print movie['title']
#     print movie['common_sense_media']
#     print ''

movies = guidebox.Movie.list(limit=250, sources='netflix')
# detail = guidebox.Movie.retrieve(id=149712)
list = json.loads(movies.__str__())
print list

print guidebox.Quota.retrieve()

# source = guidebox.Movie.retrieve(id='5108')
# test = json.loads(source.__str__())
# for each in test['cast']:
#     print each['character_name'] + ': ' + each['name']
#
# print movies




