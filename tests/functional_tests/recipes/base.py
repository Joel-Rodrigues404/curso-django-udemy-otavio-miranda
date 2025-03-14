from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from recipes.tests.test_recipe_base import RecipeMixin
from utils.browser import make_firefox_browser
import time


class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):
    def setUp(self):
        self.browser = make_firefox_browser()
        return super().setUp()

    def tearDown(self):
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)
