# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.staticfiles.testing import LiveServerTestCase

from django.db import IntegrityError

from selenium import webdriver

from pyvirtualdisplay import Display


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

class TestRecommendationsForm00(LiveServerTestCase00):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm00, self).setUp()

    def test_genre_comedy(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        genre_input = self.browser.find_element_by_name('genre')
        for option in genre_input.find_elements_by_tag_name('option'):
            if option.text == "Comedy":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm01(LiveServerTestCase01):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm01, self).setUp()

    def test_year_range(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        from_input = self.browser.find_element_by_name('from')
        for option in from_input.find_elements_by_tag_name('option'):
            if option.text == "2008":
                option.click()
                break
        to_input = self.browser.find_element_by_name('to')
        for option in to_input.find_elements_by_tag_name('option'):
            if option.text == "2008":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm02(LiveServerTestCase02):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm02, self).setUp()

    def test_rating_r(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "R":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm03(LiveServerTestCase03):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm03, self).setUp()

    def test_language_english(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        language_input = self.browser.find_element_by_name('language')
        for option in language_input.find_elements_by_tag_name('option'):
            if option.text == "English":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm04(LiveServerTestCase04):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm04, self).setUp()

    def test_netflix(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        netflix_input = self.browser.find_element_by_name('netflix')
        netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm05(LiveServerTestCase05):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm05, self).setUp()

    def test_amazon(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        amazon_input = self.browser.find_element_by_name('amazon')
        amazon_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal14235")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm06(LiveServerTestCase06):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm06, self).setUp()

    def test_year_range(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        from_input = self.browser.find_element_by_name('from')
        for option in from_input.find_elements_by_tag_name('option'):
            if option.text == "2002":
                option.click()
                break
        to_input = self.browser.find_element_by_name('to')
        for option in to_input.find_elements_by_tag_name('option'):
            if option.text == "2002":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal14235")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()

class TestRecommendationsForm07(LiveServerTestCase07):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        super(TestRecommendationsForm07, self).setUp()

    def test_year_amazon(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        from_input = self.browser.find_element_by_name('from')
        for option in from_input.find_elements_by_tag_name('option'):
            if option.text == "2002":
                option.click()
                break
        to_input = self.browser.find_element_by_name('to')
        for option in to_input.find_elements_by_tag_name('option'):
            if option.text == "2002":
                option.click()
                break
        amazon_input = self.browser.find_element_by_name('amazon')
        amazon_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal14235")
        self.browser.implicitly_wait(20)

    def tearDown(self):
        self.browser.quit()










