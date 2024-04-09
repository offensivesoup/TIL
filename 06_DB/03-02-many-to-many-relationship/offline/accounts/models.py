from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
# Create your models here.
class User(AbstractUser):
    follwings = models.ManyToManyField('self', symmetrical=False, related_name="followers")
    