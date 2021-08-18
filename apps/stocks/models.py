from django.db import models


class Stocks(models.Model):
    id = models.IntegerField('id')
    nome = models.CharField('Nome', max_length=100)
    symbol = models.CharField('Symbol', max_length=8)
