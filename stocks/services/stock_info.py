import requests


def get_stock_info_by_symbol(symbol):
    url_API = f'https://api.hgbrasil.com/finance/stock_price?key=5b9dd8e3&symbol={symbol}'
    request = requests.get(url_API)
    response = request.json()
    if response['results'][symbol].get('error') is True:
        return response['results'][symbol].get('message')
    else:
        return response


def get_stocks_info_by_symbols(symbol_list):
    """symbol_list=['BIDI4','PETR4','PETR5']"""
    list_stock = []
    for symbol in symbol_list:
        stock_info = get_stock_info_by_symbol(symbol)
        '''tratar a lista'''
        serialized_stock = serialize_stock(
            stock_info=stock_info, symbol=symbol)
        list_stock.append(serialized_stock)
    return list_stock


def serialize_stock(stock_info, symbol):
    name = stock_info['results'][symbol]['company_name']
    price = stock_info['results'][symbol]['price']
    updated_at = stock_info['results'][symbol]['updated_at']
    market_cap = stock_info['results'][symbol]['market_cap']
    change_percent = stock_info['results'][symbol]['change_percent']
    return {
        'name': name,
        'price': price,
        'symbol': symbol,
        'updated_at': updated_at.split('-')[0],
        'market_cap': market_cap,
        'change_percent': change_percent,
    }
