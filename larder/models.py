from django.db import models


class Item(models.Model):
    """
    An item for a shopping list that is in the larder.
    """

    name = models.CharField(unique=True, max_length=30)


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
