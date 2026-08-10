from django.contrib import admin

from .models import Customer, Restaurant, Items, Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Items)
admin.site.register(Cart)
