from django.http import HttpRequest
from django.shortcuts import render

from burgers.models import Burger


def burger_list(request: HttpRequest):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)

    context = {"burgers": burgers}

    return render(request, "burger_list.html", context=context)


def burger_search(request: HttpRequest):
    keyword = request.GET.get("keyword", "")
    print(keyword)

    burgers = Burger.objects.filter(name__contains=keyword)
    print(burgers)

    context = {
        "burgers": burgers,
    }

    return render(request, "burger_search.html", context=context)
