from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Character
from .forms import TokenForm

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
    token_form = TokenForm()
    return render(request, 'characters/detail.html', {
        'character': character, 'token_form': token_form
    })

class CharacterCreate(CreateView):
    model = Character
    fields = '__all__'

class CharacterUpdate(UpdateView):
    model = Character
    fields = '__all__'

class CharacterDelete(DeleteView):
    model = Character
    success_url = '/characters'

def add_token(request, character_id):
    form = TokenForm(request.POST)
    if form.is_valid():
        new_token = form.save(commit=False)
        new_token.character_id = character_id
        new_token.save()
    return redirect('detail', character_id=character_id)