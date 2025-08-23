

# Register your models here.
# students/admin.py
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll_no','grade','is_active')
    search_fields = ('name','roll_no')
    list_filter = ('grade','is_active')
