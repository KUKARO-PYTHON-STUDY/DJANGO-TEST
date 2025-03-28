from django.db import models

# Create your models here.

class Post(models.Model):
    title: models.CharField = models.CharField("포스트 제목", max_length=100)
    content: models.TextField = models.TextField("포스트 내용")
    
    def __str__(self) -> str:
        return f"Post(title={self.title}, content={self.content})"

class Comment(models.Model):
    post: models.ForeignKey = models.ForeignKey(Post, on_delete=models.CASCADE)
    content: models.TextField = models.TextField("댓글 내용")
    
    def __str__(self) -> str:
        return f"Comment(post={self.post.title}, content={self.content})"