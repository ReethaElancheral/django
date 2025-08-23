from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm, ManualSubscriberForm
from .models import Subscriber

def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have subscribed successfully!")
            return redirect("signup") 
    else:
        form = SubscriberForm()
    return render(request, "signup.html", {"form": form})


def manual_signup(request):
    if request.method == "POST":
        form = ManualSubscriberForm(request.POST)
        if form.is_valid():
            Subscriber.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
            )
            messages.success(request, "You have subscribed successfully!")
            return redirect("manual") 
    else:
        form = ManualSubscriberForm()
    return render(request, "form.html", {"form": form})
