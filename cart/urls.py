from django.urls import path, include
from . import views

urlpatterns = [
    path("myCart/<int:id>", views.myCart, name="myCart"),
    path("myCart/", views.go_to_cart, name="go_to_my_cart"),
    path("delete/<int:id>", views.delete_from_cart, name="dlt_cart"),
]
