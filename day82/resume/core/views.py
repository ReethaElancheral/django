

# Create your views here.
from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'core/resume_list.html', {'resumes': resumes})

def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'core/resume_form.html', {'form': form})
