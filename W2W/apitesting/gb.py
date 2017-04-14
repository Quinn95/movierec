import guidebox
import json

#key : e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5
guidebox.api_key = "e9eb585ff0a9c36c22b6cf0fdc0a08cccfa5eac5"
guidebox.Region = "US"

#movies = guidebox.Movie.list()

source = guidebox.Movie.retrieve(id='5108')
print source

#print movies




