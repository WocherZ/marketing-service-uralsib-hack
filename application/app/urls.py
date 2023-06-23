from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register', views.register, name='register'),
    path('authorization', views.authorization, name='authorization'),
    path('main_page', views.main_page, name='main_page'),
]
