from django.db import models

# Create your models here.

from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # gets file extension
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .pdf, .doc, .docx allowed.')

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    file = models.FileField(upload_to='resumes/', validators=[validate_file_extension])

    def __str__(self):
        return self.name
