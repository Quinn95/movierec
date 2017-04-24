# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie, Genre, Person, Language, Keyword

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(Language)
admin.site.register(Keyword)