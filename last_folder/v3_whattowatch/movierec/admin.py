# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie, Genre, Person, Language, Keyword

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['identifier', 'title']
    list_display = ['title', 'identifier', 'date', 'vote_average', 'popularity', 'netflix_available', 'amazon_available', 'hulu_available', 'hbo_available']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Language)
admin.site.register(Keyword)
