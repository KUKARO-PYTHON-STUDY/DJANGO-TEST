from django.http import HttpRequest
from django.shortcuts import render

from burgers.models import Burger


def burger_list(request: HttpRequest):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {"burgers": burgers}

    return render(request, "burger_list.html", context=context)
