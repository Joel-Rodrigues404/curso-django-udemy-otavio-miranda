from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_firefox_browser

import time


class RecipeBaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = make_firefox_browser()
        return super().setUp()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)
