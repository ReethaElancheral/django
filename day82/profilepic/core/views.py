from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'core/profile_list.html', {'profiles': profiles})

def profile_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'core/profile_form.html', {'form': form})

def home(request):
    return redirect('profile_list')  # or render a custom home page
