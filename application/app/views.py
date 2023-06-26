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
                request.session['user_group'] = get_group_by_user_login(login)
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
            create_query_history_record(description, output)
        else:
            error = 'Ошибка заполнения формы'

    context = {'form': form, 'error': error, 'output': output}

    # добавил для отладки
    # data = [
    #     {
    #         'query': 'Инвестиционный фонд с разнообразным портфелем активов, включающим акции, облигации, сырьевые товары и криптовалюты. Фонд предлагает высокую степень диверсификации и потенциал роста в различных секторах экономики.',
    #         'output': 'Инвестиционный фонд с разнообразным портфелем активов и потенциалом роста.',
    #         'query_date': '2023-06-25',
    #         'feedback': 'True'
    #     },
    #     {
    #         'query': 'Second query',
    #         'output': 'Second output',
    #         'query_date': '2023-06-26',
    #         'feedback': 'Second feedback'
    #     },
    #     {
    #         'query': 'Third query',
    #         'output': 'Third output',
    #         'query_date': '2023-06-27',
    #         'feedback': 'Third feedback'
    #     }
    # ]
    # context['data'] = data
    if request.session.get('user_group') == 'DEVELOPER':
        context['data'] = collect_query_history()

    return render(request, 'personal_page.html', context=context)

def logout(request):
    try:
        del request.session['is_auth']
        del request.session['login']
        del request.session['user_group']
    except Exception:
        print("Ошибка удалении сессии")
    return redirect('home')
