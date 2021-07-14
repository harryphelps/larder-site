from django.shortcuts import render
from rest_framework import generics

from .models import Item
from .serializers import ItemListSerializer


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
