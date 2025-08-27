from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name
