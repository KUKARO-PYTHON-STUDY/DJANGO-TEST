from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)
