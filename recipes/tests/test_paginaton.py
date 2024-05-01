from django.urls import reverse
from recipes.tests.test_recipe_base import RecipeTestBase


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

        search_url = reverse("recipes:home")
        response = self.client.get(search_url)

        expected_objects_in_page = 9
        objects_in_page = len(response.context["recipes"].object_list)

        self.assertEqual(expected_objects_in_page, objects_in_page)
