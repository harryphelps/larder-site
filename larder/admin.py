from django.contrib import admin

from .models import Item, Larder, User

admin.site.register(Item)
admin.site.register(Larder)
admin.site.register(User)
