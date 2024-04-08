from django.db import models
from django.conf import settings
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length = 100)
    like_customers = models.ManyToManyField(Customer)
    price = models.DecimalField(decimal_places = 2, max_digits = 200)
