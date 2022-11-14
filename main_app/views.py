from django.shortcuts import render

# delete later when we add data to db
characters = [
  {'name': 'SpongeBob SquarePants', 'description': 'Sponge', 'starred_in': 'SpongeBob SquarePants', },
  {'name': 'Bugs Bunny', 'description': 'Rabbit', 'starred_in': 'Looney Tunes', },
  {'name': 'Stewie Griffin', 'description': 'Evil Genius Baby', 'starred_in': 'Family Guy'},
  {'name': 'Scooby Doo', 'description': 'Dog', 'starred_in': 'Scooby Doo'},

]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def characters_index(request):
    return render(request, 'characters/index.html', {
        'characters': characters
    })