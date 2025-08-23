from django.contrib import admin

# Register your models here.
# store/admin.py

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','in_stock')
    search_fields = ('name',)
    list_filter = ('in_stock',)
