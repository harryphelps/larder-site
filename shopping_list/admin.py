from django.contrib import admin

from .models import ShoppingAuditEntry, ShoppingTrip

admin.site.register(ShoppingTrip)
admin.site.register(ShoppingAuditEntry)
