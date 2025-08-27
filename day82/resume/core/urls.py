from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),    # homepage shows uploaded resumes
    path('upload/', views.resume_create, name='resume_create'),
]
