from django.db import models


class Item(models.Model):
    """
    An item for a shopping list that is in the larder.
    """

    name = models.CharField(unique=True, max_length=30)
    last_purchased_on = models.DateField(auto_now=True)
    last_used_on = models.DateField(blank=True, null=True)
    average_shelf_life = models.IntegerField(blank=True, null=True)
    total_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.total_in_stock} in stock"
