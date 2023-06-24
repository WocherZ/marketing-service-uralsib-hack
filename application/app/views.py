from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegisterForm()
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            if not is_exist_login(login):
                create_marketer(login, password)
                return redirect('home')
            error = 'Пользователь с таким логином уже существует'
        else:
            error = 'Ошибка регистрации'

    context = {'form': form, 'error': error}
    return render(request, 'register.html', context=context)

def authorization(request):
    form = LoginForm()
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            if check_user_credentials(login, password):
                return redirect('home')
            else:
                error = 'Ошибка авторизации'

    context = {'form': form, 'error': error}
    return render(request, 'authorization.html', context=context)

def personal_page(request):
    return render(request, 'personal_page.html')
