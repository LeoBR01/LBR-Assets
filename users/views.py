from django.views.generic import TemplateView
from django.shortcuts import render
from stocks.services import stock_info

# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def searchBar(self):
        if self.request.method == 'GET':
            query = self.request.GET.get('query')
            if query:
                return query
            else:
                return None

    def get_context_data(self, *args, **kwargs):
        if self.searchBar() != None:
            context = {
                'stocks': stock_info.get_stocks_info_by_symbols([self.searchBar()]),
            }
            return context


class WalletView(TemplateView):
    template_name = 'wallet.html'
