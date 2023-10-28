from django.shortcuts import render
from utils.teste import fake_recipe
from faker import Faker


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [fake_recipe() for _ in range(10)],
})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': fake_recipe(),
})
