from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from django.urls import reverse
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuario) == 0:
        return redirect(reverse('login') + '?status=1')
    elif len(usuario) > 0:
        request.session['logado'] = True
        return redirect(reverse('home'))

def sair(request):
    request.session['logado'] = None
    return render(request, 'login.html')

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect(reverse('cadastro') + '?status=1')

    if len(senha) < 8:
        return redirect(reverse('cadastro') + '?status=2')

    usuario = Usuario.objects.filter(email=email)

    if len(usuario) > 0:
        return redirect(reverse('cadastro') + '?status=3')

    try:
        senha_criptografada = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
        usuario.save()
        return redirect(reverse('cadastro') + '?status=0')
    except:
        return redirect(reverse('cadastro') + '?status=4')
