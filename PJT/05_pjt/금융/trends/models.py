from django.db import models

# Create your models here.

class Keyword(models.Model):
    name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add = True)
    
class Trend(models.Model):
    name = models.CharField(max_length=225)
    result = models.IntegerField()
    search_period = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add = True)
    
