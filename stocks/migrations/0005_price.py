# Generated by Django 3.2.6 on 2021-08-27 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_alter_stock_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('modify', models.DateField(auto_now=True, verbose_name='Update date')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('value', models.IntegerField(verbose_name='Value')),
                ('min', models.IntegerField(verbose_name='Low Price')),
                ('max', models.IntegerField(verbose_name='Max Price')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.stock', verbose_name='Stock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
