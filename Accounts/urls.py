from django.urls import path, include
from . import views

urlpatterns = [
    path("regestration/", views.user_reg, name="user_reg"),
    path("login/", views.user_login, name="user_login"),
    path("active/<uid64>/<token>/", views.activate, name="activate"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.user_logout, name="user_logout"),
]
