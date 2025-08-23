from django.db import models

# Create your models here.
# store/models.py

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
