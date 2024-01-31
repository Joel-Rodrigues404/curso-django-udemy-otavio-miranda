from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes import factory
# Create your views here.

def home(request):
    context = {
        'recipes':[factory.make_recipe() for _ in range(10)]
    }

    return render(request, 'recipes/pages/home.html', context=context)

def recipe(request, id):

    context = {
        'recipe': factory.make_recipe(),
        'is_detail_page':True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context=context)
    