from django.views.generic import TemplateView
from .services import stock_info


class StockInfo(TemplateView):
    template_name = 'stock.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'stocks': stock_info.get_stocks_info_by_symbols(['BIDI4', 'PETR4', 'EMBR3']),
        }
        return context
