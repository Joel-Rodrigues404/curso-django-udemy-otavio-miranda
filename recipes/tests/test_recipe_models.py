from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    """Testa aspectos importantes para as view"""

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name="test_default category"),
            author=self.make_author(username="newuser"),
            title="title_recipe1",
            description="description_recipe1",
            slug="slug-recipe1",
            preparation_time=1,
            preparation_time_unit="preparation_time_unit_recipe1",
            servings=1,
            servings_unit="servings_unit_recipe1",
            preparation_steps="preparation_steps_recipe1",
        )
        recipe.save()
        recipe.full_clean()
        return recipe

    @parameterized.expand(
        [
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 65),
            ("servings_unit", 65),
        ]
    )
    def test_recipe_fields_max_leght(self, field, max_len):
        setattr(self.recipe, field, "A" * (max_len + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg="Recipe preparation_steps is not false by defalt",
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg="Recipe is_published is not false by defalt",
        )

    def test_recipe_string_representation(self):
        needed = "needed string for test"
        self.recipe.title = "needed string for test"
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(
            str(self.recipe.title),
            needed,
            msg=f"Recipe string representation must be "
            f'"{needed}" but "{str(self.recipe)}" was received.',
        )
