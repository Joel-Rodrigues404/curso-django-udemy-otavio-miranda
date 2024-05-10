from django.shortcuts import render, redirect
from django.http import Http404
from . import forms


def register_view(request):
    register_form_data = request.session.get("register_form_data", None)
    form = forms.RegisterForm(register_form_data)

    context = {"form": form}
    return render(request, "authors/pages/register_view.html", context=context)


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = forms.RegisterForm(POST)

    return redirect("authors:register")
