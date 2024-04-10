from django.db import models
from django.contrib.auth.models import User

# Create your models here for items
## Category tag
class Category(models.Model):
    name = models.CharField(max_length=255)

    # handles the appearance in the admin pane
    class Meta:
        ordering = ('name',) # this statement orders the categories by alphabet
        verbose_name_plural = 'Categories' # spelling Categories correctly in admin left side pane

    # showing the actual name of the category in admin panel
    def __str__(self):
        return self.name

## Item tag
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # category of item
    name = models.CharField(max_length=255) # name of item
    description = models.TextField(blank=True, null=True) # item description
    price = models.FloatField() # price of item
    image = models.ImageField(upload_to='item_images', blank=True, null=True) # item image
    is_sold = models.BooleanField(default=False) # has item been sold
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # who created
    created_at = models.DateTimeField(auto_now_add=True) # when was item created

    # showing the actual item of the category in admin panel
    def __str__(self):
        return self.name