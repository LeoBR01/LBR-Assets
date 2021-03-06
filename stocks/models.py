from django.db import models


class Base(models.Model):
    created = models.DateField('Creation Date', auto_now_add=True)
    modify = models.DateField('Update date', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Stock(Base):
    name = models.CharField('Name', max_length=100)
    symbol = models.CharField('Symbol', max_length=8)

    def __str__(self):
        return self.name


class Price(Base):
    value = models.IntegerField('Value')
    min = models.IntegerField('Low Price')
    max = models.IntegerField('Max Price')
    stock = models.ForeignKey(
        'stocks.Stock', verbose_name='Stock', on_delete=models.CASCADE)
