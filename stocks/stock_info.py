import requests


def getInfo(symbol):

    url_API = f'https://api.hgbrasil.com/finance/stock_price?key=5b9dd8e3&symbol={symbol}'
    r = requests.get(url_API)
    data = r.json()
    return data
