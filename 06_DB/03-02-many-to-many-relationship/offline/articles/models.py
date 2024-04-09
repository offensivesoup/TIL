from django.db import models
from django.conf import settings
# Create your models here.
# 파이썬 기본 변수명 등의 컨벤션만 잘 지켜도 헷갈릴 일은 없다.
# Model class를 class에 상속한다.

class Article(models.Model):
    # 작성자 정보를 담기위한 1:N 관계
    # User Model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")
    title = models.TextField()
    content = models.TextField()
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    content = models.CharField(max_length = 100)