from django.views.generic import TemplateView
from .services import stock_info


class StockInfo(TemplateView):
    template_name = 'stock.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'stocks': [stock_info.get_info('BIDI4')],
        }
        return context
