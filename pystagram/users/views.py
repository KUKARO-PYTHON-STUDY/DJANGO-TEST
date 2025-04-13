from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from users.forms import LoginForm


def login_view(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        return redirect("/posts/feeds/")

    if request.method == "POST":
        return login_view_post(request)
    else:
        return login_view_get(request)


def login_view_post(request: HttpRequest) -> HttpResponse:
    form = LoginForm(data=request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("/posts/feeds")
        else:
            print("로그인에 실패했습니다")
            form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다")

    context = {"form": form}
    return render(request, "users/login.html", context)


def login_view_get(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(("/users/login/"))
