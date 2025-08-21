from django.db import models

# Create your models here.
# inventory/models.py

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # keep in_stock synced with quantity
        self.in_stock = self.quantity > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({'In Stock' if self.in_stock else 'Out of Stock'})"
