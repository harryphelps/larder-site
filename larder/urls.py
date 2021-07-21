from django.urls import path

from . import views

urlpatterns = [
    path("", views.ItemListAPIView.as_view(), name="item_list"),
    path("<int:id>/", views.ItemDetailAPIView.as_view(), name="item_detail"),
    path("create/", views.ItemCreateAPIView.as_view(), name="item_create"),
    path(
        "update/<int:id>/",
        views.ItemRetrieveUpdateAPIView.as_view(),
        name="item_update",
    ),
    path("delete/<int:id>/", views.ItemDestroyAPIView.as_view(), name="item_delete"),
]
