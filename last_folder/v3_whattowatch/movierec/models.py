from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Person(models.Model):
    identifier = models.IntegerField(default = -1)
    name = models.CharField(max_length = 50, default = 'SOME STRING')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Genre(models.Model):
    identifier = models.IntegerField(default = -1)
    name = models.CharField(max_length = 50, default = 'SOME STRING')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Language(models.Model):
    name = models.CharField(max_length = 2, default = 'N/A')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Keyword(models.Model):
    name = models.CharField(max_length = 200, default = '')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Movie(models.Model):
    identifier = models.IntegerField(unique = True)
    themoviedb = models.IntegerField(null = True)
    imdb = models.CharField(max_length = 200, null = True)
    rating = models.CharField(max_length = 7)
    rottentomatoes = models.IntegerField(null = True)
    metacritic = models.CharField(max_length = 200, null = True)
    common_sense_media = models.CharField(max_length = 200, null = True)
    poster = models.CharField(max_length = 200, null = True)
    title = models.CharField(max_length = 200, null = True)
    summary = models.CharField(max_length = 2500, null = True, blank = True)
    runtime = models.IntegerField(null = True, blank = True)
    budget = models.IntegerField(null = True, blank = True)
    vote_count = models.IntegerField(null = True, blank = True)
    vote_average = models.DecimalField(decimal_places = 2, max_digits = 4, null = True, blank = True)
    popularity = models.DecimalField(decimal_places = 2, max_digits = 4, null = True, blank = True)
    genre = models.ManyToManyField(Genre)
    people = models.ManyToManyField(Person)
    date = models.IntegerField(null= True)
    languages = models.ManyToManyField(Language) #may change
    netflix = models.CharField(max_length = 200, null = True, blank = True)
    netflix_available = models.BooleanField(default = False)
    amazon = models.CharField(max_length = 200, null = True, blank = True)
    amazon_available = models.BooleanField(default = False)
    hulu = models.CharField(max_length = 200, null = True, blank = True)
    hulu_available = models.BooleanField(default = False)
    hbo = models.CharField(max_length = 200, null = True, blank = True)
    hbo_available = models.BooleanField(default = False)
    trailer = models.CharField(max_length = 200, null = True)
    keywords = models.ManyToManyField(Keyword)
    tmdb_get = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.netflix:
            self.netflix = None
        if not self.amazon:
            self.amazon = None
        if not self.hulu:
            self.hulu = None
        super(Movie, self).save(*args, **kwargs)

