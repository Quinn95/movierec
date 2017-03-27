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
    title = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Person)
    directors = models.ManyToManyField(Person)
    date = models.DateField()
    language = models.CharField(max_length=2) #may change

    def __str__(self):
        return self.title
