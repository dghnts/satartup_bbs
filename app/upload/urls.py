from django.urls import path
from . import views

app_name = "upload"

urlpatterns = [
    path('album/', views.album, name="album"),
    path('document/', views.document, name="document"),
]