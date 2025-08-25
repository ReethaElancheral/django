from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'posted_on')
    search_fields = ('title', 'description')
    ordering = ('-posted_on',)
