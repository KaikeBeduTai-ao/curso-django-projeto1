from django.shortcuts import render
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Kaike Taiao'})

def contato(request):
    return render(request, 'me-apague/temp.html')

def sobre(request):
    return render(request, 'recipes/sobre.html')