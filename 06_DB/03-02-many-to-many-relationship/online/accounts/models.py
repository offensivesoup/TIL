from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 참조 : 내가 팔로우하는 사람들
    # 역참조 : 나를 팔로우하는 사람들
    followings = models.ManyToManyField('self', symmetrical = False, related_name='followers')
