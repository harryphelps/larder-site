from django.db import models


class Item(models.Model):
    """
    An item for a shopping list that is in the larder.
    """

    name = models.CharField(max_length=30)


class ShoppingTrip(models.Model):
    """
    A list of items bought in a shop.
    """

    visited_on = models.DateField()
    money_spent = models.DecimalField(max_digits=6, decimal_places=2)


class Larder(models.Model):
    """
    A list of items with quanitites in stock in the larder.
    """

    item = models.ForeignKey(Item)
    total_in_stock = models.IntegerField()


class User(models.Model):
    """
    A user of the larder service
    """

    user_name = models.CharField()
    larder_id = models.ForeignKey(Larder)


class ShoppingAuditEntry(models.Model):
    """
    A table linking the items to a shopping trip.
    """

    item = models.ForeignKey(Item)
    shopping_trip = models.ForeignKey(ShoppingTrip)
    quantity_bought = models.IntegerField()
    user_id = models.ForeignKey(User)
