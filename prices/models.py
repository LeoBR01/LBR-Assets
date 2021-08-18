from django.db import models


class Base(models.Model):
    created = models.DateField('Creation Date', auto_now_add=True)
    modify = models.DateField('Update date', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Price(Base):
    value = models.IntegerField('Value')
    min = models.IntegerField('Low Price')
    max = models.IntegerField('Max Price')
    stock = models.ForeignKey(
        'stocks.Stock', verbose_name='Stock', on_delete=models.CASCADE)
