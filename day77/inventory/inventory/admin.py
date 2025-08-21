from django.contrib import admin

# Register your models here.
# inventory/admin.py

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "quantity", "in_stock")
    list_filter = ("in_stock",)
    search_fields = ("name",)
    ordering = ("-id",)
