from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    if request.session.get('logado'):
        return render(request, 'home.html')
    else:
        messages.add_message(request, constants.WARNING, 'Faça o login para entrar na aplicação')
        return redirect(reverse('login'))
        
