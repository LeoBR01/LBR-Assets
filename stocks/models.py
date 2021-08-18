from django.db import models


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificar = models.DateField('Data de Atualiazação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Stocks(Base):
    id = models.IntegerField('id', primary_key=True)
    nome = models.CharField('Nome', max_length=100)
    symbol = models.CharField('Symbol', max_length=8)

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return self.nome
