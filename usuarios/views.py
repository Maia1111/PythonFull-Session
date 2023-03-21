from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from django.urls import reverse
from hashlib import sha256
from django.contrib import messages
from django.contrib.messages import constants


def login(request):   
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        messages.add_message(request, messages.ERROR, 'Email ou senha inválidos.')
        return redirect(reverse('login'))
    elif len(usuario) > 0:
        request.session['logado'] = True
        request.session['usuario_id'] = usuario[0].id 
        messages.add_message(request, constants.SUCCESS, 'Você entrou em nossa pagina, sejam bem vindos!')      
        return redirect(reverse('home'))

def sair(request):   
    request.session.flush()
    request.session['logado'] = False    
    messages.add_message(request, messages.SUCCESS, 'Você saiu da aplicação.')   
    return render(request, 'login.html')
   


def cadastro(request):       
        status = request.GET.get('status')
        return render(request, 'cadastro.html', {'status': status})
       
    
    


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.WARNING,'Os campos email e senha não podem ser vazios!')
        return redirect(reverse('cadastro'))
        

    if len(senha) < 8:
        messages.add_message(request, constants.WARNING,'A senha deve ter no minimo 8 caracteres!')
        return redirect(reverse('cadastro'))

    usuario = Usuario.objects.filter(email=email)

    if len(usuario) > 0:
       messages.add_message(request, constants.WARNING,'Já existe um usuário com este email')
       return redirect(reverse('login'))


    try:
        senha_criptografada = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect(reverse('cadastro'))        
    except:
        messages.add_message(request, constants.SUCCESS, 'Erro interno do sistema')
        return redirect(reverse('cadastro'))
