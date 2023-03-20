from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.session['logado']:
        return HttpResponse("Voces esta no sistema!")
    else:
        return HttpResponse("Você não esta logado!")

