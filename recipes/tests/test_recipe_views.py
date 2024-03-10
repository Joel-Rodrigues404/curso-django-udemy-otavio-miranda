""" Testa as Views de recipes """

from unittest import skip
from django.urls import reverse, resolve
from recipes.tests.test_recipe_base import RecipeTestBase
from .. import views


class RecipeViewTest(RecipeTestBase):
    """Testa aspectos importantes para as view"""

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

    # -=--=-=--=-=--=-=--= Recipe View -=--=-=--=-=--=-=--=-=--=-=--=
    def test_recipes_recipe_view_fuctions_is_correct(self):
        """Vejo se a url '/' e direcionada para a função views.home"""
        view = resolve(reverse("recipes:recipe", kwargs={"recipe_id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_returns_404_if_no_recipes(self):
        """Testa se a pagina home tem status code 200"""
        response = self.client.get(reverse("recipes:recipe", kwargs={"recipe_id": 100}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_template_loads_recipes(self):
        """Testa se o conteudo desejado e renderizado na aplicação"""
        needed_title = "This is a recipe test - it render one recipe"
        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1})
        )
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)

    def test_recipes_recipe_template_dont_load_recipes_not_published(self):
        """Testa se a receita não marcada com is_pub ira ser renderizada"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:recipe", kwargs={"recipe_id": recipe.id})
        )
        self.assertEqual(response.status_code, 404)

    # -=--=-=--=-=--=-=--= Category View -=--=-=--=-=--=-=--=-=--=-=--=
    def test_recipes_category_view_fuctions_is_correct(self):
        """Vejo se a url '/' e direcionada para a função views.home"""
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, views.category)

    def test_recipes_category_view_returns_404_if_no_recipes(self):
        """Testa se a pagina home tem status code 200"""
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipes_category_template_loads_recipes(self):
        """Testa se o conteudo desejado e renderizado na aplicação"""
        needed_title = "This is a category test"
        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1})
        )
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)

    def test_recipes_category_template_dont_load_recipes_not_published(self):
        """Testa se a receita não marcada com is_pub ira ser renderizada"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": recipe.category.id})
        )
        self.assertEqual(response.status_code, 404)

    # -=--=-=--=-=--=-=--= Others -=--=-=--=-=--=-=--=-=--=-=--=
    @skip("WIP")
    def test_test_for_skip(self):
        """Teste para skipar"""
        assert 1 == 1

        # Se Eu ainda tiver que escrever mais algum codigo
        self.fail("Tem que fazer tal tal tal ...")
