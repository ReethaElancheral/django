from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        "name": "Reetha",
        "title": "Full-Stack Developer",
        "email": "nisha.reetha30@gmail.com",
        "phone": "+91 9043765615",
        "website": "https://reethamannavan.github.io/Project/Portfolio/pages/about.html",
        "linkedin": "https://linkedin.com/in/reetha",
        "github": "https://github.com/ReethaElancheral",
    }
    return render(request, "profile.html", context)
