from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


def index(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_authenticated:
        return redirect("/posts/feeds/")
    return redirect("/users/login/")
