# Generated by Django 3.2.6 on 2021-08-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificar', models.DateField(auto_now=True, verbose_name='Data de Atualiazação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('symbol', models.CharField(max_length=8, verbose_name='Symbol')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]