from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Job

# Dashboard (only logged-in users)
@login_required
def dashboard_view(request):
    return render(request, 'portal/dashboard.html')

# Register
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'portal/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'portal/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

# Jobs list
@login_required
def jobs_view(request):
    jobs = Job.objects.all()
    return render(request, 'portal/jobs.html', {'jobs': jobs})

# Job detail
@login_required
def job_detail_view(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'portal/job_detail.html', {'job': job})


from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required

@login_required
def jobs_view(request):
    jobs = Job.objects.all().order_by('-posted_on')  # make sure you query all jobs
    return render(request, 'portal/jobs.html', {'jobs': jobs})
