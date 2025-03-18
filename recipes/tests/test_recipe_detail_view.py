from django.urls import reverse, resolve
from recipes.tests.test_recipe_base import RecipeTestBase
from .. import views
import pytest


class RecipeDetailViewTest(RecipeTestBase):
    """Testa aspectos importantes para a view de detail"""

    # -=--=-=--=-=--=-=--= Recipe View -=--=-=--=-=--=-=--=-=--=-=--=
    def test_recipes_recipe_view_fuction_is_correct(self):
        """Vejo se a url '/' e direcionada para a função views.home"""
        view = resolve(reverse("recipes:recipe", kwargs={"recipe_id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_returns_404_if_no_recipes_found(self):
        """Testa se a pagina home tem status code 200"""
        response = self.client.get(
            reverse("recipes:recipe", kwargs={"recipe_id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_template_loads_the_correct_recipes(self):
        """Testa se o conteudo desejado e renderizado na aplicação"""
        needed_title = "This is a recipe test - it render one recipe"
        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse("recipes:recipe", kwargs={"recipe_id": 1})
        )
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)

    def test_recipes_recipe_detail_template_dont_load_recipes_not_published(self):
        """Testa se a receita não marcada com is_pub ira ser renderizada"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:recipe", kwargs={"recipe_id": recipe.id})
        )
        self.assertEqual(response.status_code, 404)
