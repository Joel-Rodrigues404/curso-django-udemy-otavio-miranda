from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from authors.forms import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login


def register_view(request):

    register_form_data = request.session.get("register_form_data", None)
    form = RegisterForm(register_form_data)

    context = {"form": form, "form_action": reverse("authors:register_create")}
    return render(request, "authors/pages/register_view.html", context=context)


def register_create(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session["register_form_data"] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, "Your user is created, please log in.")

        del request.session["register_form_data"]

        return redirect(reverse('authors:login'))

    return redirect("authors:register")


def login_view(request):
    form = LoginForm()
    context = {"form": form, "form_action": reverse("authors:login_create")}
    return render(request, "authors/pages/login.html", context=context)


def login_create(request):

    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse("authors:login")

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get("username", ""),
            password=form.cleaned_data.get("password", ""),
        )

        if authenticated_user is not None:
            messages.success(request, "You are logged in.")
            login(request, authenticated_user)
        else:
            messages.error(request, "Invalid credentials")
    else:
        messages.error(request, "Invalid username or password")

    return redirect(login_url)
