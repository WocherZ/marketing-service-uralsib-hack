from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def authorization(request):
    return render(request, 'authorization.html')
