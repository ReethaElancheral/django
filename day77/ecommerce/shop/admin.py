from django.contrib import admin

# Register your models here.
# shop/admin.py
from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "in_stock")
    list_filter = ("in_stock", "category")
    search_fields = ("name", "description")
    list_editable = ("in_stock",)
    ordering = ("name",)
    autocomplete_fields = ("category",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    autocomplete_fields = ("product",)
    fields = ("product", "quantity", "unit_price", "line_total")
    readonly_fields = ("line_total",)

    def line_total(self, obj):
        try:
            return obj.quantity * obj.unit_price
        except Exception:
            return 0
    line_total.short_description = "Line total"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "created_at", "item_count", "total_amount_display")
    list_filter = ("created_at",)
    search_fields = ("customer_name", "email")
    date_hierarchy = "created_at"
    inlines = [OrderItemInline]
    readonly_fields = ("summary_total",)

    def total_amount_display(self, obj):
        return obj.total_amount
    total_amount_display.short_description = "Total"

    def summary_total(self, obj):
        if not obj.pk:
            return "—"
        return f"Total amount: {obj.total_amount} (items: {obj.item_count})"
    summary_total.short_description = "Order Summary"
