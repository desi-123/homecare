# Generated by Django 4.1.7 on 2023-03-20 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
