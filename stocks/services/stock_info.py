import requests
import json

list_stock = []


def get_info(symbol):
    url_API = f'https://api.hgbrasil.com/finance/stock_price?key=5b9dd8e3&symbol={symbol}'
    request = requests.get(url_API)
    response = request.json()
    if response['results'][symbol].get('error') is True:
        return response['results'][symbol].get('message')
    else:
        list_stock.append(response)
        return response


chamada = get_info('BIDI4')


def new_list_stock(lista):
    for stock in lista:
        symbol = stock['results'][symbol]
        name = stock['results'][symbol]['company_name']
        price = stock['results'][symbol]['market_cap']['price']

    print(name, symbol, price)


new_list_stock(list_stock)
