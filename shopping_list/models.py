from django.db import models


class Item(models.Model):
    """
    An item for a shopping list that is in the larder.
    """

    name = models.CharField(unique=True, max_length=30)


class ShoppingTrip(models.Model):
    """
    A list of items bought in a shop.
    """

    visited_on = models.DateField(auto_now=True)
    money_spent = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)


class Larder(models.Model):
    """
    A list of items with quanitites in stock in the larder.
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_in_stock = models.IntegerField()


class User(models.Model):
    """
    A user of the larder service
    """

    user_name = models.CharField(max_length=30)
    larder_id = models.ForeignKey(Larder, on_delete=models.CASCADE)


class ShoppingAuditEntry(models.Model):
    """
    A table linking the items to a shopping trip.
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    shopping_trip = models.ForeignKey(ShoppingTrip, on_delete=models.CASCADE)
    quantity_bought = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
