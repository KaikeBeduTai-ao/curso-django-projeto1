from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page')

def contato(request):
    return HttpResponse('Contato Page')

def sobre(request):
    return HttpResponse('Sobre Page')