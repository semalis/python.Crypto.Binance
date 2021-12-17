# https://algotrading101.com/learn/binance-python-api-guide/

from binance.client import Client

import configparser

# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('../secret.cfg'))
api_key = config.get('BINANCE', 'API_KEY')
api_secret = config.get('BINANCE', 'SECRET_KEY')

client = Client(api_key, api_secret)

# get latest price from Binance API
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
# print full output (dictionary)
print(btc_price)

print(btc_price["price"])
