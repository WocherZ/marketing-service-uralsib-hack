from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('authorization', views.authorization, name='authorization'),
    path('personal_page', views.personal_page, name='personal_page'),
    path('logout', views.logout, name='logout'),
]
