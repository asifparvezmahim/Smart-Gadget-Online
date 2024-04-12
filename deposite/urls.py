from django.urls import path, include
from . import views

urlpatterns = [path("deposite_form/", views.depo_form, name="depo_form")]
