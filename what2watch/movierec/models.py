from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Person(models.Model):
    identifier = models.IntegerField(default=-1)
    name = models.CharField(max_length=50, default='SOME STRING')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Genre(models.Model):
    identifier = models.IntegerField(default=-1)
    name = models.CharField(max_length=50, default='SOME STRING')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Movie(models.Model):
    identifier = models.IntegerField(unique=True)
    themoviedb = models.IntegerField(null=True)
    imdb = models.CharField(max_length=200, null=True)
    rating = models.CharField(max_length=7)
    rottentomatoes = models.IntegerField(null=True)
    wikipedia_id = models.IntegerField(null=True)
    metacritic = models.CharField(max_length=200, null=True)
    common_sense_media = models.CharField(max_length=200, null=True)
    poster = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=30, null=True)
    genre = models.ManyToManyField(Genre)
    people = models.ManyToManyField(Person)
    date = models.IntegerField(null=True)
    language = models.CharField(max_length=2, null=True) #may change
    netflix = models.CharField(max_length=200, null=True)
    amazon = models.CharField(max_length=200, null=True)
    hulu = models.CharField(max_length=200, null=True)
    trailer = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
