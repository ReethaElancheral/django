from django.db import models

# Create your models here.
# students/models.py


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=10, unique=True)
    grade = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
