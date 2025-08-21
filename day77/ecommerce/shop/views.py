from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    category_id = request.GET.get("category")
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        active_category = int(category_id)
    else:
        products = Product.objects.all()
        active_category = None

    categories = Category.objects.all()
    return render(
        request,
        "shop/product_list.html",
        {
            "products": products,
            "categories": categories,
            "active_category": active_category,
        },
    )
