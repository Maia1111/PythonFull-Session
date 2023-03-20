from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def home(request):
    if request.session['logado']:
        return HttpResponse("Voces esta na Home!")
    else:
        return redirect(reverse('login') + '?status=2') 
