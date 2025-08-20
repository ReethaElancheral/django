from django.shortcuts import render

# Create your views here.


def home(request):
    skills = ["Python", "Django", "React", "TailwindCSS"]
    return render(request, "myapp/home.html", {"skills": skills})

def about(request):
    return render(request, "myapp/about.html")

def projects(request):
    project_list = [
        {"name": "Portfolio Website", "desc": "Built with Django"},
        {"name": "E-Commerce App", "desc": "Flask + Stripe"},
        {"name": "Meditation Site", "desc": "React + Tailwind"},
    ]
    return render(request, "myapp/projects.html", {"projects": project_list})

def contact(request):
    return render(request, "myapp/contact.html")
