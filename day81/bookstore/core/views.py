from django.shortcuts import render

# Create your views here.

from .models import Author, Book, Category

def author_list(request):
    authors = Author.objects.all()
    return render(request, "core/author_list.html", {"authors": authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, "core/book_list.html", {"books": books})

def category_list(request):
    categories = Category.objects.all()
    return render(request, "core/category_list.html", {"categories": categories})

def home(request):
    return render(request, "core/home.html")
