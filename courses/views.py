from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm
from .models import AudioFile, Notebook, Section, Video


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if request.is_ajax():
                return JsonResponse({'success': True})
            return redirect('thenumerixsocial')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
def home(request):
    notebooks = Notebook.objects.all()
    return render(request, 'home.html', {'notebooks': notebooks})

def notebook_detail(request, notebook_id):
    notebook = get_object_or_404(Notebook, id=notebook_id)
    sections = Section.objects.filter(notebook=notebook)
    return render(request, 'notebook_detail.html', {'notebook': notebook, 'sections': sections})

def section_detail(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    audio_files = AudioFile.objects.filter(section=section)
    videos = Video.objects.filter(section=section)
    return render(request, 'section_detail.html', {'section': section, 'audio_files': audio_files, 'videos': videos})
