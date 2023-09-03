from django.urls import path
from . import views

app_name = "bbs"
urlpatterns = [
    path("", views.index, name="index"),
    path("bbs/", views.bbs, name="bbs"),
    path("single/<int:pk>/", views.single, name="single"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("album/", views.album, name="album"),
    path("document/", views.document, name="document"),
    path("calendar", views.calendar, name="calendar")
]
