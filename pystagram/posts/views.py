from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def feeds(request: HttpRequest) -> HttpResponse:
    user = request.user
    if not user.is_authenticated:
        return redirect("/users/login/")
    return render(request, "posts/feeds.html")
