from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

def home(request):
    if request.session.get('logado'):
        return render(request, 'home.html')
    else:
        return redirect(reverse('login') + '?status=2')
