from binance.client import Client

import configparser

# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('../secret.cfg'))
api_key = config.get('BINANCE', 'API_KEY')
api_secret = config.get('BINANCE', 'SECRET_KEY')

client = Client(api_key, api_secret)
# client.API_URL = 'https://binance.vision/api'
# print(client.get_account())
print(client.get_asset_balance(asset='BTC'))
