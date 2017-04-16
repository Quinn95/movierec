from django.contrib import admin

# Register your models here.

from .models import Movie, Genre, Person

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Person)

