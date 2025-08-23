
# store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm



def home(request):
    return redirect('product-list')


# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# Product detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

# Create product
def product_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    return render(request, 'store/product_form.html', {'form': form})

# Update product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    return render(request, 'store/product_form.html', {'form': form})

# Delete product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product-list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})
