from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes import factory
from .models import Recipe
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q
from utils.recipes.pagination import make_pagination_range

# Create your views here.


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")

    try:
        current_page = request.GET.get("page", 1)
    except ValueError:
        current_page = 1

    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        qty_pages=4,
        current_page=current_page
    )

    context = {
        "x": [factory.make_recipe() for _ in range(10)],
        "recipes": page_obj,
        "pagination_range": pagination_range,
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

    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": get_recipe,
            "is_detail_page": True,
        },
    )


def search(request):
    search_term = request.GET.get("q", "").strip()

    if not search_term:
        raise Http404()

    # title__contains=search_term,  # Diferencia maiusculas de minusculas
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) | Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by("-id")

    return render(
        request,
        "recipes/pages/search.html",
        context={
            "page_title": f'search for "{search_term}"',
            "search_term": search_term,
            "recipes": recipes,
        },
    )
