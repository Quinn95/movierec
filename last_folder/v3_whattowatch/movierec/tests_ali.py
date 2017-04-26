class TestRecommendationsForm(LiveServerTestCase):
    def setUp(self):
        #self.display = Display(visible=0, size=(1024, 768))
        #self.display.start()

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

        super(TestRecommendationsForm, self).setUp()

    def test_get_recommendations_action(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        genre_input = self.browser.find_element_by_name('genre')
        for option in genre_input.find_elements_by_tag_name('option'):
            if option.text == "Action":
                option.click()
                break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_id("myModal34688")
        self.browser.implicitly_wait(20)
        #from_input = self.browser.find_element_by_name('from')
        #to_input = self.browser.find_element_by_name('to')

    #this is a new test by Ali Momin
    def test_get_language_english(self):
        self.browser.get("http://localhost:8000/movierec/form/")
        lang_input = self.browser.find_element_by_name('language')
        for lang in lang_input.find_elements_by_tag_name('option'):
        	if lang.text == "English":
        		lang.click()
        		break
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("myModal34688")
        self.browser.implicitly_wait(20)

    def test_get_netflix_movies(self):
    	self.browser.get("http://localhost:8000/movierec/form/")
        stream_input = self.browser.find_element_by_name('netflix')
        stream_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("myModal34688")
        self.browser.implicitly_wait(20)

    def test_get_amazon_movies(self):
    	self.browser.get("http://localhost:8000/movierec/form/")
        stream_input = self.browser.find_element_by_name('amazon')
        stream_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("#needschange")
        self.browser.implicitly_wait(20)

    def test_get_hulu_movies(self):
    	self.browser.get("http://localhost:8000/movierec/form/")
        stream_input = self.browser.find_element_by_name('hulu')
        stream_input.click()
        submit_input = self.browser.find_element_by_name('Submit')
        submit_input.click()
        modal = self.browser.find_element_by_name_id("#needschange")
        self.browser.implicitly_wait(20)


    def tearDown(self):
        self.browser.quit()
        #self.display.stop()