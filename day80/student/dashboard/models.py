from django.db import models

# Create your models here.

from django.conf import settings

class Attendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    present = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date} - {'Present' if self.present else 'Absent'}"

class Grade(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='grades')
    course = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['course']

    def __str__(self):
        return f"{self.user.username} - {self.course}: {self.score}"
