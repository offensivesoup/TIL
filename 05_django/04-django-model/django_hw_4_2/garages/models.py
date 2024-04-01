from django.db import models

class garages_garage(models.Model):
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    is_parking_avaliable = models.BooleanField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    
# Create your models here.
