# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.contrib.staticfiles.testing import LiveServerTestCase

from django.db import IntegrityError

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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



class TestRecommendationsForm(LiveServerTestCase):
    def setUp(self):
        #self.display = Display(visible=0, size=(1024, 768))
        #self.display.start()

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

        super(TestRecommendationsForm, self).setUp()
'''
    def test_get_netflix_movies(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
        #stream_input = self.browser.find_element_by_name('netflix')

        self.browser.execute_script("if($('#netflix').css('border') == '0px none rgb(255, 255, 255)'){ $('#netflix').css({\"border\": \"2px solid orange\"}); $( \"input[name='\"netflix\"']\" ).prop(\"checked\", true); } else if($('#netflix').css('border') == '2px solid rgb(255, 165, 0)'){ $('#netflix').css({\"border\": \"0px none rgb(255, 255, 255)\"}); $( \"input[name='\"netflix\"']\" ).prop(\"checked\", false); };")
        #stream_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("myModal34688")
        self.browser.implicitly_wait(200)
'''

    def tearDown(self):
        self.browser.quit()
        #self.display.stop()





    def test_get_recommendations_action(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
        genre_input = self.browser.find_element_by_name('genre')
        for option in genre_input.find_elements_by_tag_name('option'):
            if option.text == "Action":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        #Tropic thunder should show up
        with not self.assertRaises(NoSuchElementException):
            modal = self.browser.find_element_by_id("myModal34688") 
        self.browser.implicitly_wait(20)
        #from_input = self.browser.find_element_by_name('from')
        #to_input = self.browser.find_element_by_name('to')

        #this is a new test by Ali Momin

    def test_get_language_english(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
        lang_input = self.browser.find_element_by_name('language')
        for lang in lang_input.find_elements_by_tag_name('option'):
            if lang.text == "English":
                lang.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("myModal34688")
        self.browser.implicitly_wait(20)

"""    
    def test_get_amazon_movies(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
        stream_input = self.browser.find_element_by_name('amazon')
        stream_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("myModal61261")
        self.browser.implicitly_wait(20)

    def test_get_hulu_movies(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
        stream_input = self.browser.find_element_by_name('hulu')
        stream_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("myModal4627")
        self.browser.implicitly_wait(20)
"""
    def test_year_range(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
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

    def test_rating_r(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "R":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

"""
    def test_year_amazon(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
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
"""
"""
    def test_back_to_back(self):

        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")

        genre_input = self.browser.find_element_by_name('genre')
        for option in genre_input.find_elements_by_tag_name('option'):
            if option.text == "Comedy":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

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

        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "R":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

        language_input = self.browser.find_element_by_name('language')
        for option in language_input.find_elements_by_tag_name('option'):
            if option.text == "English":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

        netflix_input = self.browser.find_element_by_name('netflix')
        netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

        amazon_input = self.browser.find_element_by_name('amazon')
        amazon_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal14235")
        self.browser.implicitly_wait(20)

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
        netflix_input = self.browser.find_element_by_name('netflix')
        netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

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
        genre_input = self.browser.find_element_by_name('genre')
        for option in genre_input.find_elements_by_tag_name('option'):
            if option.text == "Action":
                option.click()
                break
        user_input = self.browser.find_element_by_name('imdb')
        for option in user_input.find_elements_by_tag_name('option'):
            if option.text == "6-8":
                option.click()
                break
        language_input = self.browser.find_element_by_name('language')
        for option in language_input.find_elements_by_tag_name('option'):
            if option.text == "English":
                option.click()
                break
        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "R":
                option.click()
                break
        netflix_input = self.browser.find_element_by_name('netflix')
        netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)

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
        user_input = self.browser.find_element_by_name('imdb')
        for option in user_input.find_elements_by_tag_name('option'):
            if option.text == "6-8":
                option.click()
                break
        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "PG-13":
                option.click()
                break
        netflix_input = self.browser.find_element_by_name('amazon')
        netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal14235")
        self.browser.implicitly_wait(20)
        self.browser.implicitly_wait(20)
"""

    def test_chicago(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
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
        user_input = self.browser.find_element_by_name('imdb')
        for option in user_input.find_elements_by_tag_name('option'):
            if option.text == "6-8":
                option.click()
                break
        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "PG-13":
                option.click()
                break
        # netflix_input = self.browser.find_element_by_name('amazon')
        # netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal14235")


    def test_tropic_thunder(self):
        self.browser.get("http://immense-fortress-33702.herokuapp.com/movierec/form/")
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
        genre_input = self.browser.find_element_by_name('genre')
        for option in genre_input.find_elements_by_tag_name('option'):
            if option.text == "Action":
                option.click()
                break
        user_input = self.browser.find_element_by_name('imdb')
        for option in user_input.find_elements_by_tag_name('option'):
            if option.text == "6-8":
                option.click()
                break
        language_input = self.browser.find_element_by_name('language')
        for option in language_input.find_elements_by_tag_name('option'):
            if option.text == "English":
                option.click()
                break
        rating_input = self.browser.find_element_by_name('rating')
        for option in rating_input.find_elements_by_tag_name('option'):
            if option.text == "R":
                option.click()
                break
        # netflix_input = self.browser.find_element_by_name('netflix')
        # netflix_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)







