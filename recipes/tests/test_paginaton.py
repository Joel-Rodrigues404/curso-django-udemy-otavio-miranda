from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse
from unittest.mock import patch
import os


class PaginationTest(RecipeTestBase):
    """Testa aspectos importantes para as a paginação"""

    def test_equal_number_of_objects_on_the_page_per_page(self):
        """testa se a quantidade de objetos na pagina e igual ao atributo per page"""
        for i, x in enumerate(range(11)):
            self.make_recipe(
                title=f"title{i}",
                slug=f"slug-{i}",
                author_data={"username": f"username-{i}"},
            )

        with patch("recipes.views.PER_PAGE", new=9):
            search_url = reverse("recipes:home")
            response = self.client.get(search_url)

            expected_objects_in_page = int(os.environ.get("PER_PAGE", 6))
            objects_in_page = len(response.context["recipes"].object_list)

            self.assertEqual(expected_objects_in_page, objects_in_page)
