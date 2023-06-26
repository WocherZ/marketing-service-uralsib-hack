import datetime
from django.db import models
from django.utils import timezone

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


def get_group_by_user_login(login):
    return User.objects.filter(login=login).first().group


FEEDBACK_CHOICES = (
    ('LIKE', 'like'),
    ('DISLIKE', 'dislike')
)
class QueryHistory(models.Model):
    query = models.TextField()
    output = models.TextField()
    query_date = models.DateTimeField(default=timezone.now())
    feedback = models.CharField(max_length=8, choices=FEEDBACK_CHOICES, null=True)

    def __str__(self):
        return self.query + " " + str(self.query_date)


def create_query_history_record(query, output):
    record = QueryHistory(query=query, output=output)
    record.save()


def collect_query_history():
    all_history = []
    records = QueryHistory.objects.all()
    for record in records:
        all_history.append({
            'query': record.query,
            'output': record.output,
            'query_date': record.query_date,
            'feedback': record.feedback
        })
    return all_history

