from django.urls import reverse, resolve
from recipes.tests.test_recipe_base import RecipeTestBase
from .. import views


class RecipeSearchViewTest(RecipeTestBase):
    """Testa aspectos importantes para as view"""

    # -=--=-=--=-=--=-=--= Search View -=--=-=--=-=--=-=--=-=--=-=--=
    def test_recipe_search_uses_correct_view_function(self):
        """Vejo se a url 'recipes/search/' e direcionada para a função views.search"""
        url = reverse("recipes:search")
        resolved = resolve(url)
        self.assertEqual(resolved.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        """Testa se a view de search rendeziza a função correta"""
        url = reverse("recipes:search") + "?q=dfa"
        response = self.client.get(url)
        self.assertTemplateUsed(response, "recipes/pages/search.html")

    def test_recipe_search_raises_404_if_no_search_term(self):
        """Testa se e retornado um erro 404 se o queryset e vazio para search"""
        response = self.client.get(reverse("recipes:search"))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        """Verifica se os termos passados no search estão sendo tratados contra xss"""
        url = reverse("recipes:search") + "?q=<teste>"
        response = self.client.get(url)
        self.assertIn(
            "search for &quot;&lt;teste&gt;&quot;", response.content.decode("utf-8")
        )

    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = "This is recipe one"
        title2 = "This is recipe two"

        recipe1 = self.make_recipe(
            title=title1, slug="one", author_data={"username": "one"}
        )
        recipe2 = self.make_recipe(
            title=title2, slug="two", author_data={"username": "two"}
        )

        search_url = reverse("recipes:search")
        response1 = self.client.get(f"{search_url}?q={title1}")
        response2 = self.client.get(f"{search_url}?q={title2}")
        response_both = self.client.get(f"{search_url}?q=This")

        self.assertIn(recipe1, response1.context["recipes"])
        self.assertNotIn(recipe2, response1.context["recipes"])

        self.assertIn(recipe2, response2.context["recipes"])
        self.assertNotIn(recipe1, response2.context["recipes"])

        self.assertIn(recipe2, response_both.context["recipes"])
        self.assertIn(recipe1, response_both.context["recipes"])
