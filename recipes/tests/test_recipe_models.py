from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeModelTest(RecipeTestBase):
    """Testa aspectos importantes para as view"""

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raise_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = "A" * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_fields_max_leght(self):
        fields = [
            ("", 65),
        ]