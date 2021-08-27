from django.contrib import admin
from .models import Price, Stock


@admin.register(Stock)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'created', 'modify', 'active')


@admin.register(Price)
class PricesAdmin(admin.ModelAdmin):
    list_display = ('value', 'min', 'max', 'stock',
                    'created', 'modify', 'active')
