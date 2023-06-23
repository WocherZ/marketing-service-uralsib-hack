from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        context = {}

        return render(request, 'base_template.html', context)

def register(request):
    return render(request, 'register.html')

def authorization(request):
    return render(request, 'authorization.html')

def main_page(request):
    return render(request, 'base_template.html')

