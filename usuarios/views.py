from django.shortcuts import render
from django.http  import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


def login(request):
   return render(request, 'login.html')
  



def cadastro(requests):
    return render(requests, 'cadastro.html')



def valida_cadastro(request):
   
   nome = request.POST.get('nome')
   email = request.POST.get('email')
   senha = request.POST.get('senha')
   
   # Verificando se  nome e email não é vazio
   if len(nome.strip()) == 0 or len(email.strip()) == 0:
      return redirect('auth/login/?status=1')
   
   # Verificando senha senha não é menor que 8 
   if len(senha) < 8:
      return redirect('auth/login/?status=2')
      
      
   # Buscando no banco bando se o email digitado no cadastro ja não tem no banco 
   usuario = Usuario.objects.filter(email = email)

   # Verificando se existe email igual ao digitado no cadastro
   if len(usuario) > 0:
      return redirect('auth/login/?status=3')
   
   
   try:
      # criptografando a senha 
      senha_criptografada = sha256(senha.encode()).hexdigest()   
      # Instanciando a usuario
      usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)   
      # Salvando no bando de dados
      usuario.save()      
      return redirect('auth/login/?status=0')
   
   except:
        return redirect('auth/login/?status=4')


   
  
   
