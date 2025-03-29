from django.contrib import admin

from blog.models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "thumbnail"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
