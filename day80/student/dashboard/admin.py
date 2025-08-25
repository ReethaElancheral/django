from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Attendance, Grade

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user','date','present')
    list_filter = ('present',)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('user','course','score')
    search_fields = ('user__username','course')
