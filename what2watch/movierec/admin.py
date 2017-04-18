from django.contrib import admin

# Register your models here.

from .models import Movie, Genre, Person, Language, Keyword

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Language)
admin.site.register(Keyword)
