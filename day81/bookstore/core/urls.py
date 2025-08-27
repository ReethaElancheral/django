from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('categories/', views.category_list, name='category_list'),
    path('', views.home, name='home'),

]
