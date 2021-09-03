from django.urls import path

from .views import StockInfo

urlpatterns = [
    path('stock/', StockInfo.as_view(template_name='stock.html'),
         name='stock'),
]
