from django.db import models

# Create your models here.
USER_GROUPS = (
    ('DEVELOPER', 'developer'),
    ('MARKETER', 'marketer'),
)

class User(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    group = models.CharField(max_length=32, choices=USER_GROUPS)

    def __str__(self):
        return self.login + " " + self.group

def create_marketer(login, password):
    marketer = User(login=login, password=password, group='MARKETER')
    marketer.save()

def create_developer(login, password):
    developer = User(login=login, password=password, group='DEVELOPER')
    developer.save()

def is_exist_login(login):
    user = User.objects.filter(login=login)
    return user.exists()

def check_user_credentials(login, password):
    user = User.objects.filter(login=login).filter(password=password)
    return user.exists()
