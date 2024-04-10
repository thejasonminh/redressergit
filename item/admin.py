from django.contrib import admin

from .models import Category, Item
# Register your models here.

# being able to manipulate Categories and Items on admin page
admin.site.register(Category)
admin.site.register(Item)