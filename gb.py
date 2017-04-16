import guidebox
import json


guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"


movielist = guidebox.Movie.list(limit=5)

movies = json.loads(movielist)

print movies
