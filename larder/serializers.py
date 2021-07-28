from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ["id", "name", "total_in_stock", "absolute_url"]

    def get_absolute_url(self, obj):
        return reverse("item_detail", args=(obj.pk,))


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "total_in_stock",
            "last_purchased_on",
            "last_used_on",
            "average_shelf_life",
        ]
