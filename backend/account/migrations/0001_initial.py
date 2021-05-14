# Generated by Django 3.2 on 2021-05-14 19:23

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
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('pnone_no', models.CharField(max_length=10)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('student_discount_date', models.DateField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_trusted', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('unique_key', models.CharField(default='', max_length=20)),
                ('unique_key_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]