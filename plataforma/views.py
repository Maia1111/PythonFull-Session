from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants
# importando os decoratrs que vamos usar na função home para entrar somente se estiver logado
from django.contrib.auth.decorators import login_required

@login_required (login_url='login')
def home(request):    
       return render(request, 'home.html')
   