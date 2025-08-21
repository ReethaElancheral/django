from django.shortcuts import render

# Create your views here.
# inventory/views.py
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by("-id")
    return render(request, "inventory/product_list.html", {"products": products})
