from django.shortcuts import render
from .models import Character

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {
        'characters': characters
    })

def characters_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    return render(request, 'characters/detail.html', {
        'character': character
    })