from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=200, default='https://placehold.co/600x400?text=No+Image')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()