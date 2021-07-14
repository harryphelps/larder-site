from rest_framework import serializers

from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "name", "total_in_stock"]
