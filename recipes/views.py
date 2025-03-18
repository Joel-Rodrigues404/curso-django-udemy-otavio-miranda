"""
View configuration for app recipes.
"""

import os
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from django.db.models import Q
from utils.recipes.pagination import make_pagination
from utils.recipes import factory
from .models import Recipe


PER_PAGE = int(os.environ.get("PER_PAGE", 6))


def home(request):
    """Trata da visualização da home"""

    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    context = {
        "x": [factory.make_recipe() for _ in range(10)],
        "pagination_range": pagination_range,
        "recipes": page_obj,
    }

    return render(request, "recipes/pages/home.html", context=context)


def category(request, category_id):
    """Trata da visualização da home filtrada por categoria"""

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True
        ).order_by("-id")
    )

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    context = {
        "title": f"{recipes[0].category.name} | Category | ",
        "x": [factory.make_recipe() for _ in range(10)],
        "pagination_range": pagination_range,
        "recipes": page_obj,
    }

    return render(request, "recipes/pages/category.html", context=context)


def recipe(request, recipe_id):
    """Trata da visualização de detalhes de uma recipe"""

    recipe = get_object_or_404(
        Recipe, id=recipe_id, is_published=True
    )

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    """Trata da logica de pesquisa"""

    search_term = request.GET.get("q", "").strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(Q(title__icontains=search_term) | Q(
            description__icontains=search_term),),
        is_published=True,
    ).order_by("-id")

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    context = {
        "additional_url_query": f"&q={search_term}",
        "page_title": f'search for "{search_term}"',
        "pagination_range": pagination_range,
        "search_term": search_term,
        "recipes": page_obj,
    }

    return render(request, "recipes/pages/search.html", context=context)
