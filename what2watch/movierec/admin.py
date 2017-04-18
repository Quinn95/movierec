from django.contrib import admin

# Register your models here.

from .models import Movie, Genre, Person, Language

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Language)

