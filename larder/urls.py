from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListAPIView.as_view(), name="item_list"),
]
