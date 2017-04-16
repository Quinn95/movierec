from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name

@python_2_unicode_compatible
class Genre(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Movie(models.Model):
    identifier = models.IntegerField(unique=True)
    themoviedb = models.IntegerField()
    imdb = models.CharField(max_length=200)
    rating = models.CharField(max_length=7)
    rottentomatoes = models.IntegerField()
    wikipedia_id = models.IntegerField()
    metacritic = models.CharField(max_length=200)
    common_sense_media = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
    title = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Person)
    #directors = models.ManyToManyField(Person)
    date = models.IntegerField()
    language = models.CharField(max_length=2) #may change

    def __str__(self):
        return self.title
