from django.urls import path
from . import views

urlpatterns = [
    path("", views.starter, name="starter"),
]