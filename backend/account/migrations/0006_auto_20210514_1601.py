# Generated by Django 3.2 on 2021-05-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210514_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='pnone_no',
            field=models.CharField(default='8899106088', max_length=10),
        ),
        migrations.AddField(
            model_name='account',
            name='student_discount_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
