from django.db import models

# shop/models.py
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return f"{self.name} ({self.category})"


class Order(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Many-to-many to Product via OrderItem (so we can store quantity/price per line)
    items = models.ManyToManyField(Product, through="OrderItem", related_name="orders")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} - {self.customer_name}"

    @property
    def total_amount(self):
        return sum(item.subtotal for item in self.order_items.all())

    @property
    def item_count(self):
        return sum(item.quantity for item in self.order_items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Captured at time of order"
    )

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def save(self, *args, **kwargs):
        # If unit_price not provided, snapshot current product price
        if self.unit_price in (None, 0):
            self.unit_price = self.product.price
        super().save(*args, **kwargs)

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"
