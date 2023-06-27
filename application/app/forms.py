from django import forms
from .models import User


class RegisterForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))


class LoginForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))


class GetMarketingProductForm(forms.Form):
    # product_description = forms.Textarea(attrs={'placeholder': 'Введите описание продукта'})
    product_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите описание продукта'}))

class GetFeedback(forms.Form):
    like = forms.BooleanField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Like'}))
    dislike = forms.BooleanField()
