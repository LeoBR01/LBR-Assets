from django.urls import path

from .views import DashboardView, WalletView


urlpatterns = [
    path('dashboard/', DashboardView.as_view(
        template_name='dashboard.html'), name='dashboard'),

    path('wallet/', WalletView.as_view(
        template_name='wallet.html'), name='wallet'),
]
