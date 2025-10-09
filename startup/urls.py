from django.urls import path
from startup import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_post, name="add_post"),
    path("<int:id>/", views.blog_detail, name="blog_detail"),
    path("<int:id>/edit/", views.edit_post, name="edit_post"),
    path("<int:id>/delete/", views.delete, name="delete"),
     
    
]
