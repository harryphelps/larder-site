from django.db import models
from larder import models as larder_models


class ShoppingTrip(models.Model):
    """
    A list of items bought in a shop.
    """

    visited_on = models.DateField(auto_now=True)
    money_spent = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)


class ShoppingAuditEntry(models.Model):
    """
    A table linking the items to a shopping trip.
    """

    item = models.ForeignKey(larder_models.Item, on_delete=models.CASCADE)
    shopping_trip = models.ForeignKey(ShoppingTrip, on_delete=models.CASCADE)
    quantity_bought = models.IntegerField()
    user_id = models.ForeignKey(larder_models.User, on_delete=models.CASCADE)
