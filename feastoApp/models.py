from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.TextField(default='https://placehold.co/600x400?text=No+Image')
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()
    
class Items(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    vegetarian = models.BooleanField(default=False)
    picture = models.TextField(default='https://placehold.co/600x400?text=No+Image')

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart")
    items = models.ManyToManyField('Items', related_name="carts")
    def total_price(self):
        return sum(item.price for item in self.items.all())
    