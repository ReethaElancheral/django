from django.shortcuts import render
import random

def index(request):
    quotes = [
        "Believe you can and you're halfway there.",
        "Do what you can with what you have, wherever you are.",
        "You are stronger than you think.",
        "The best way to get started is to quit talking and begin doing.",
        "Dream big and dare to fail.",
        "Stay positive, work hard, make it happen.",
        "Small steps every day lead to big results."
    ]
    quote = random.choice(quotes)
    return render(request, "index.html", {"quote": quote})

def about(request):
    context = {
        "title": "About Us",
        "content": "This Daily Quotes Website provides daily motivation to inspire and encourage users. Built with Django and Bootstrap, it’s simple, fast, and responsive."
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
        "title": "Contact Us",
        "content": "You can reach us via email: support@dailyquotes.com or follow us on social media for daily updates."
    }
    return render(request, "contact.html", context)
