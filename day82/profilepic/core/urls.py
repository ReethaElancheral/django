from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # maps root URL
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/add/', views.profile_create, name='profile_create'),
]
