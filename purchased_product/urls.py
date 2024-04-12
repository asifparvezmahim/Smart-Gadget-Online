from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "purchased_product_from_product_section/<int:id>/",
        views.purchased_product_from_product_section,
        name="purchased_from_product_section",
    ),
    path(
        "purchased_product_from_details_section/<int:id>/",
        views.purchased_product_from_details_section,
        name="purchased_from_details_section",
    ),
]
