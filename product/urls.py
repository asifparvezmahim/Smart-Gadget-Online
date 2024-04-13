from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.diplay_products, name="display_products"),
    path(
        "category/<slug:category_slug>/",
        views.diplay_products,
        name="category_wise_products",
    ),
    path("details/<int:id>/", views.details_page, name="details"),
]
