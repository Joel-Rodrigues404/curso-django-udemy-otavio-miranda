from django.urls import reverse, resolve
from recipes.tests.test_recipe_base import RecipeTestBase
from .. import views


class RecipeHomeViewTest(RecipeTestBase):
    """Testa aspectos importantes para a view de home"""

    # -=--=-=--=-=--=-=--= Home View -=--=-=--=-=--=-=--=-=--=-=--=
    def test_recipes_home_view_fuctions_is_correct(self):
        """Vejo se a url '/' e direcionada para a função views.home"""
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipes_home_view_returns_status_code_200_ok(self):
        """Testa se a pagina home tem status code 200"""
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_view_loads_correct_template(self):
        """Testa se o template renderizado e o correto"""
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipes_home_template_shows_no_recipe_found_if_no_recipe(self):
        """Testa o caso de não haver receitas na pagina de home"""
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h1> No Recipes found here :) </h1>", response.content.decode("utf-8")
        )

    def test_recipes_home_template_dont_load_recipes_not_published(self):
        """Testa se a receita não marcada com is_pub ira ser renderizada"""
        self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h1> No Recipes found here :) </h1>", response.content.decode("utf-8")
        )

    def test_recipes_home_template_loads_recipes(self):
        """Testa se o conteudo desejado e renderizado na aplicação"""
        self.make_recipe()
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")
        response_context_recipes = response.context["recipes"]

        self.assertIn("title_recipe1", content)
        self.assertEqual(len(response_context_recipes), 1)