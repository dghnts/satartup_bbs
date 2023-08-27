from django.urls import path
from . import views

app_name = "bbs"
urlpatterns = [
    path("", views.bbs, name="bbs"),
    path("single/<int:pk>", views.single, name="single"),
]
