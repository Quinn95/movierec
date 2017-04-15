import guidebox
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

movies = guidebox.Movie.list()

# source = guidebox.Movie.retrieve(id='5108')
print movies
# test = json.loads(source.__str__())
# for each in test['cast']:
#     print each['character_name'] + ': ' + each['name']
#
# print movies




