# Generated by Django 4.1.7 on 2023-03-19 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]