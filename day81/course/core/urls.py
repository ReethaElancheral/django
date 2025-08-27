from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('lessons/', views.lesson_list, name='lesson_list'),
]
