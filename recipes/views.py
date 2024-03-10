from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes import factory
from .models import Recipe

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    context = {
        "x": [factory.make_recipe() for _ in range(10)],
        "recipes": recipes,
    }

    return render(request, "recipes/pages/home.html", context=context)


def category(request, category_id):
    # category_name = getattr(getattr(recipes.first(), 'category', None), 'name',
    # 'Not Found') # noqa
    # if not recipes:
    #     raise Http404('Not Found :)')
    #     return HttpResponse(content='Not Found', status=404)
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by(
            "-id"
        )
    )

    context = {
        "x": [factory.make_recipe() for _ in range(10)],
        "recipes": recipes,
        "title": f"{recipes[0].category.name} | Category | ",
        # 'title': f'{category_name} | Category | '
    }

    return render(request, "recipes/pages/category.html", context=context)


def recipe(request, recipe_id):
    get_recipe = get_object_or_404(Recipe, id=recipe_id, is_published=True)

    context = {
        "recipe": get_recipe,
        "is_detail_page": True,
    }
    return render(request, "recipes/pages/recipe-view.html", context=context)
