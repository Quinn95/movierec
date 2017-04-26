# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, StaticLiveServerTestCase

from django.db import IntegrityError

from selenium.webdriver.firefox.webdriver import WebDriver


from .models import Movie

# Create your tests here.


class TestMovieModel(TestCase):
    def createMovie(self, title="Test Movie", identifier=1, rating="PG"):
        return Movie.objects.create(title=title, identifier=identifier,
                                    rating=rating)

    def test_movie_creation(self):
        m = self.createMovie()
        self.assertTrue(isinstance(m, Movie))
        self.assertEqual(m.__str__(), m.title)


    def test_unique_id_collision(self):
        m1 = self.createMovie()
        with self.assertRaises(IntegrityError):
            m2 = self.createMovie()


    def test_netflix_link_and_variable1(self):
        m = self.createMovie()
        m.netflix_available = True
        m.netflix = "http://blah"
        m.save()

        if m.netflix_available:
            self.assertEquals(m.netflix_available, (m.netflix is not None))

    def test_netflix_link_and_variable2(self):
        m = self.createMovie()
        m.netflix_available = True
        m.save()

        if m.netflix_available:
            self.assertTrue(m.netflix is None)

    def test_movie_query_by_title(self):
        m = self.createMovie()
        m1 = self.createMovie(title="Test Movie 2", identifier=2,
                             rating="NC-17")
        result = Movie.objects.get(title="Test Movie")
        self.assertEquals(1, result.identifier)

class TestRecommendationsForm(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = WebDriver()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_get_recommendations(self):
        self.browser.get("/movierec/form/")
        genre = "Any"
        







