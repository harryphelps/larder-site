from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListAPIView.as_view(), name="item_list"),
    path("<int:id>/", views.ItemDetailAPIView.as_view(), name="item_detail"),
]
