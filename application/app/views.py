from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
import requests

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
                request.session['is_auth'] = True
                request.session['login'] = login
                request.session['group'] = getattr(User.objects.filter(login=login).first(), 'group')
                return redirect('home')
            else:
                error = 'Ошибка авторизации'

    context = {'form': form, 'error': error}
    return render(request, 'authorization.html', context=context)


API_MODEL_URL = 'localhost:8001'
def personal_page(request):
    form = GetMarketingProductForm()
    error = ''
    output = ''
    if request.method == 'POST':
        form = GetMarketingProductForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('product_description')
            # TODO - отправка description в api модели
            # response = requests.post(API_MODEL_URL, json={'text': description})
            # output = response.json().get('json').get('output')
            output = "# TODO - здесь будет выход модели"
        else:
            error = 'Ошибка заполнения формы'

    context = {'form': form, 'error': error, 'output': output}
    return render(request, 'personal_page.html', context=context)

def logout(request):
    try:
        del request.session['is_auth']
        del request.session['login']
        del request.session['group']
    except Exception:
        print("Ошибка удалении сессии")
    return redirect('home')
