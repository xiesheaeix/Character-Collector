from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Character, Award
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
    id_list = character.awards.all().values_list('id')
    awards_character_doesnt_have = Award.objects.exclude(id__in=id_list)
    token_form = TokenForm()
    return render(request, 'characters/detail.html', {
        'character': character, 'token_form': token_form,
        'awards': awards_character_doesnt_have
    })

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'description', 'starred_in', 'image_path']

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

class AwardList(ListView):
    model = Award

class AwardDetail(DetailView):
    model = Award

class AwardCreate(CreateView):
    model = Award
    fields = '__all__'

class AwardUpdate(UpdateView):
    model = Award
    fields = ['name']

class AwardDelete(DeleteView):
    model = Award
    success_url = '/awards'

def assoc_award(request, character_id, award_id):
    Character.objects.get(id=character_id).awards.add(award_id)
    return redirect('detail', character_id=character_id)

def unassoc_award(request, character_id, award_id):
    Character.objects.get(id=character_id).awards.remove(award_id)
    return redirect('detail', character_id=character_id)
