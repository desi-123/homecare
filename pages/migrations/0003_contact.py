# Generated by Django 4.1.7 on 2023-03-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_description_about_description_one_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('description_one', models.TextField(blank=True)),
                ('description_two', models.TextField(blank=True)),
                ('description_three', models.TextField(blank=True)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
            ],
        ),
    ]
