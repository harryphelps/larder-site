from django.shortcuts import render
from rest_framework import generics

from .models import Item
from .serializers import ItemDetailSerializer, ItemListSerializer


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class ItemDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
