from django.urls import path, include
from . import views

urlpatterns = [
    path("products/", views.diplay_products, name="display_products"),
    path("details/<int:id>/", views.details_page, name="details"),
]
