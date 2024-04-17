from django.urls import path, include
from . import views
from .views import save_review

urlpatterns = [
    path("review/<int:id>/", views.save_review, name="myRev"),
]
