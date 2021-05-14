# Generated by Django 3.2 on 2021-04-14 19:57

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=32, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('unique_key', models.CharField(default='', max_length=20)),
                ('key_time', models.DateTimeField(auto_now_add=True, verbose_name='Unique Key Requested At')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
