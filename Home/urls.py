from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("load_all_from/home/", views.load_all, name="load_all"),
]
