from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, ManualContactForm
from .models import Contact

def home(request):
    return render(request, "contact/home.html")  # app folder name included

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect("contact_form")
    else:
        form = ContactForm()
    return render(request, "contact/contact_form.html", {"form": form})

def manual_contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, "Message sent successfully!")
            return redirect("manual_contact_form")
        else:
            messages.error(request, "All fields are required.")
    return render(request, "contact/manual_form.html")
