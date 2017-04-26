# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Movie, Person, Genre, Language, Keyword

# Create your tests here.

class MovieTest(TestCase):
	def setUp(self):
		Movie.objects.create(title = "Iron Man",
							 summary = "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
							 imdb = "http://www.imdb.com/title/tt0371746/",
							 rating = "PG-13",
							 runtime = 126)
		Movie.objects.create(title = "Thor",
							 summary = "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
							 imdb = "http://www.imdb.com/title/tt0800369/",
							 rating = "PG-13",
							 runtime = 115)

	def test_0(self):
		