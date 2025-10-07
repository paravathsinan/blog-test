from django.urls import path
from startup import views

urlpatterns = [
    path("", views.index, name="index"),
]
