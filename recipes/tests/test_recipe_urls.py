""" Testa as Urls de recipes """

from django.test import TestCase
from django.urls import reverse


class RecipeUrlsTest(TestCase):
    """Testa se as Urls estão como o esperado"""

    def test_recipes_home_url_is_correct(self):
        """Testa se a "recipes:home" e igual a "/" """
        url = reverse("recipes:home")
        self.assertEqual(url, "/")

    def test_recipes_category_url_is_correct(self):
        """Testa se a "recipes:category" com id 1 e igual a "/recipes/category/1/" """  # noqa E501
        url = reverse("recipes:category", kwargs={"category_id": 1})
        self.assertEqual(url, "/recipes/category/1/")

    def test_recipes_recipe_url_is_correct(self):
        """Testa se a "recipes:recipe" com id 1 e igual a '/recipes/1/'"""
        url = reverse("recipes:recipe", kwargs={"recipe_id": 1})
        self.assertEqual(url, "/recipes/1/")
