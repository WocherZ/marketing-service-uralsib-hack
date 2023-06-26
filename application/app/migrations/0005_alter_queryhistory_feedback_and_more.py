# Generated by Django 4.2.2 on 2023-06-26 23:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_queryhistory_query_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryhistory',
            name='feedback',
            field=models.CharField(choices=[('LIKE', 'like'), ('DISLIKE', 'dislike')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='queryhistory',
            name='query_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 23, 7, 47, 866380, tzinfo=datetime.timezone.utc)),
        ),
    ]
