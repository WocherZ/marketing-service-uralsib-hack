# Generated by Django 4.2.2 on 2023-06-25 22:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_queryhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryhistory',
            name='query_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 25, 22, 57, 51, 878595, tzinfo=datetime.timezone.utc)),
        ),
    ]