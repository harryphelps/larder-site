from rest_framework import serializers

from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "total_in_stock"]


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
