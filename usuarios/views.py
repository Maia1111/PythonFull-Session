from django.shortcuts import render
from django.http  import HttpResponse


def login(request):
   return render(request, 'login.html')
  



def cadastro(requests):
    return render(requests, 'cadastro.html')



