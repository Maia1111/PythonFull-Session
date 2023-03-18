from django.shortcuts import render
from django.http  import HttpResponse
from .models import Usuario


def login(request):
   return render(request, 'login.html')
  



def cadastro(requests):
    return render(requests, 'cadastro.html')



def valida_cadastro(request):
   
   nome = request.POST.get('nome')
   email = request.POST.get('email')
   senha = request.POST.get('senha')
   return HttpResponse(f"{nome} {email} {senha}")

