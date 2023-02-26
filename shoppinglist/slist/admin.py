from django.contrib import admin
from .models import ShoppingList, UserList, Item, MallList

# Register your models here.

admin.site.register(ShoppingList)
admin.site.register(UserList)
admin.site.register(Item)
admin.site.register(MallList)
