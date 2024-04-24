from django.urls import reverse, resolve
from recipes.tests.test_recipe_base import RecipeTestBase
from .. import views


class RecipeCategoryViewTest(RecipeTestBase):
    """Testa aspectos importantes para a view de category"""

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
        response = self.client.get(reverse("recipes:category", args=(1,)))
        content = response.content.decode("utf-8")

        self.assertIn(needed_title, content)

    def test_recipes_category_template_dont_load_recipes_not_published(self):
        """Testa se a receita não marcada com is_pub ira ser renderizada"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": recipe.category.id})
        )
        self.assertEqual(response.status_code, 404)
