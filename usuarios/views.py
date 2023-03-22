from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Usuario
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valida_login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    usuario = authenticate(username=nome, password=senha)

    if usuario is None:
        messages.add_message(request, messages.ERROR, 'Nome ou senha inválidos.')
        return redirect(reverse('login'))

    login(request)
    messages.add_message(request, constants.SUCCESS, 'Você entrou em nossa página, sejam bem vindos!')
    request.session['logado'] = True
    return redirect(reverse('home'))


def sair(request):
    request.session.flush()
    request.session['logado'] = False
    messages.add_message(request, messages.SUCCESS, 'Você saiu da aplicação.')
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        messages.add_message(request, constants.WARNING, 'Os campos email e senha não podem ser vazios!')
        return redirect(reverse('cadastro'))

    if len(senha) < 8:
        messages.add_message(request, constants.WARNING, 'A senha deve ter no mínimo 8 caracteres!')
        return redirect(reverse('cadastro'))

    if User.objects.filter(email=email).exists():
        messages.add_message(request, constants.WARNING, 'Já existe um usuário com este email.')
        return redirect(reverse('cadastro'))

    if User.objects.filter(username=nome).exists():
        messages.add_message(request, constants.WARNING, 'Já existe um usuário com este nome.')
        return redirect(reverse('cadastro'))

    try:
        usuario = User.objects.create_user(username=nome, email=email, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect(reverse('cadastro'))
    except:
        messages.add_message(request, constants.SUCCESS, 'Erro interno do sistema')
        return redirect(reverse('cadastro'))
