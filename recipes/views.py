from django.shortcuts import render
from utils.recipes import factory
from .models import Recipe
# Create your views here.


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    context = {
        'x': [factory.make_recipe() for _ in range(10)],
        'recipes': recipes
    }

    return render(request, 'recipes/pages/home.html', context=context)


def recipe(request, id):
    context = {
        'recipe': factory.make_recipe(),
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context=context)
