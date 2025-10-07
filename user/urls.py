from django.urls import path
from user import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('profile/', views.profile, name='profile'),
    
]

