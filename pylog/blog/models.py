from django.db import models

# Create your models here.


class Post(models.Model):
    title: models.CharField = models.CharField("포스트 제목", max_length=100)
    content: models.TextField = models.TextField("포스트 내용")
    thumbnail: models.ImageField = models.ImageField("썸네일 이미지", upload_to="post", blank=True)

    def __str__(self) -> str:
        return f"Post(title={self.title}, content={self.content}, thumbnail={self.thumbnail})"


class Comment(models.Model):
    post: models.ForeignKey = models.ForeignKey(Post, on_delete=models.CASCADE)
    content: models.TextField = models.TextField("댓글 내용")

    def __str__(self) -> str:
        return f"Comment(post={self.post.title}, content={self.content})"
