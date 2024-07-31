from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class StudentTestCase(LiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument('–headless')
        self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_student_find_solos(self):
        """
        Test that a user can search for solos
        """
        # Steve is a jazz student who would like to find more
        # examples of solos so he can improve his own
        # improvisation. He visits the home page of JMAD.
        home_page = self.browser.get(self.live_server_url + '/')
        # He knows he's in the right place because he can see
        # the name of the site in the heading.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, ".navbar-brand")
        self.assertEqual('JMAD', brand_element.text)
        # He sees the inputs of the search form, including
        # labels and placeholders.
        instrument_input = self.browser.find_element(By.CSS_SELECTOR, "input#jmad-instrument")
        self.assertEqual(instrument_input.get_attribute('placeholder'), 'i.e. trumpet')
        artist_input = self.browser.find_element(By.CSS_SELECTOR,'input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element(By.CSS_SELECTOR, 'label[for="jmad-artist"]'))
        self.assertEqual(artist_input.get_attribute('placeholder'), 'i.e. Davis')
        # He types in the name of his instrument and submits
        # it.
        instrument_input.send_keys('saxophone')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        # He sees too many search results...
        # ...so he adds an artist to his search query and
        # gets a more manageable list.
        search_results = self.browser.find_elements(By.CSS_SELECTOR, '.jmad-search-result')
        self.assertGreater(len(search_results), 2)
        second_artist_input = self.browser.find_element(By.CSS_SELECTOR, 'input#jmad-artist')
        second_artist_input.send_keys('Cannonball Adderley')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()
        second_search_results = self.browser.find_elements(By.CSS_SELECTOR, '.jmad-search-result')
        self.assertEqual(len(second_search_results), 2)
        self.fail('Incomplete Test')
        # He clicks on a search result.
        # The solo page has the title, artist and album for
        # this particular solo.
        # He also sees the start time and end time of the
        # solo.