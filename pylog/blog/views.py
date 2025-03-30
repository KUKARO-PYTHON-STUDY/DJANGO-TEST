from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from blog.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "post_list.html", context)


def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    context = {
        "post_id": post_id,
        "post": post,
    }
    return render(request, "post_detail.html", context)


def post_add(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        post = Post.objects.create(
            title=title,
            content=content,
        )
        return redirect(f"/posts/{post.id}/")
    return render(request, "post_add.html")
