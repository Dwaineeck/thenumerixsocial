import json
import os
from threading import Thread

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .create_video import create_video_parallel
from .forms import DocumentForm, UserRegisterForm
from .models import AudioFile, Document
from .process_notebook import (handle_uploaded_file, process_notebook,
                               process_notebook_and_create_audio)

progress_data = {}

def home(request):
    # Retrieve all uploaded audio files
    uploaded_files = AudioFile.objects.all()  # Adjust this based on your actual model

    context = {
        'uploaded_files': uploaded_files
    }
    return render(request, 'boaapp/home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'boaapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'boaapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def handle_audio_creation(file_path, file_name):
    global progress_data
    audio_files = list(process_notebook_and_create_audio(file_path))
    total_files = len(audio_files)
    
    for idx, audio_file in enumerate(audio_files):
        if isinstance(audio_file, dict):
            title = audio_file.get('title')
            if title:
                audio_file_path = os.path.join('audio', title + '.mp3')
                with open(audio_file_path, 'w') as f:
                    f.write(audio_file['content'])
                progress_data[file_name] = {'progress': int((idx + 1) / total_files * 100)}
                print(f"Audio content written to {audio_file_path}")
        else:
            print(f"Unexpected data type found in audio_files: {type(audio_file)}")
    
    progress_data[file_name] = {'progress': 100, 'completed': True}
    print("Sections and audio files created.")

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['uploaded_file'])
            
            # Process the notebook and create audio files
            response_data = list(process_notebook_and_create_audio(file_path))
            
            # Determine the final progress or completion response
            final_response = response_data[-1]
            
            if isinstance(final_response, dict) and final_response.get('message') == 'Sections and audio files created.':
                # If successful, render the success page
                return render(request, 'boaapp/upload_success.html')
    else:
        form = DocumentForm()
    return render(request, 'boaapp/upload.html', {'form': form})

def upload_success(request):
    return render(request, 'boaapp/upload_success.html')

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path

def process_audio_and_create_videos(audio_dir, video_dir, logo_path, background_path):
    audio_files = sorted([os.path.join(audio_dir, file) for file in os.listdir(audio_dir) if file.endswith('.mp3')])
    
    for audio_file in audio_files:
        section = process_notebook(file_path)  # Adjust as needed
        output_file = os.path.join(video_dir, f"{os.path.basename(audio_file).replace('.mp3', '.mp4')}")
        text_sync_file = os.path.join(video_dir, f"{os.path.basename(audio_file).replace('.mp3', '.json')}")
        
        create_video_parallel(section, audio_file, output_file, logo_path, background_path, text_sync_file)
    
    print("Video creation complete.")

@csrf_exempt
def upload_progress(request):
    # Simulate progress or implement real-time progress logic
    progress = 100  # Just an example
    if progress >= 100:
        return redirect('upload_success')
    return render(request, 'boaapp/upload_progress.html', {'progress': progress})
