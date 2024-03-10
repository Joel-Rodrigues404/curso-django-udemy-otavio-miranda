from django.test import TestCase
from ..models import Recipe, Category, User


class RecipeTestBase(TestCase):
    def setUp(self) -> None:  # pylint: disable=W0246
        return super().setUp()

    def make_category(self, name="name_categoru_1") -> Category:
        return Category.objects.create(name=name)

    def make_author(
        self,
        first_name="firstname1",
        last_name="lastname1",
        username="username1",
        email="user1@email.com",
        password="123456",
    ) -> User:

        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

    def make_recipe(
        self,
        category_data=None,
        author_data=None,
        title="title_recipe1",
        description="description_recipe1",
        slug="slug-recipe1",
        preparation_time=1,
        preparation_time_unit="preparation_time_unit_recipe1",
        servings=1,
        servings_unit="servings_unit_recipe1",
        preparation_steps="preparation_steps_recipe1",
        preparation_steps_is_html=False,
        is_published=True,
    ) -> Recipe:

        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published,
        )
