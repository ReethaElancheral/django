from django.shortcuts import render

# Create your views here.

from .models import Course, Teacher, Lesson

def course_list(request):
    courses = Course.objects.all()
    return render(request, "core/course_list.html", {"courses": courses})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "core/teacher_list.html", {"teachers": teachers})

def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, "core/lesson_list.html", {"lessons": lessons})

def home(request):
    return render(request, "core/home.html")
