from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

import configparser

# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('../secret.cfg'))
api_key = config.get('BINANCE', 'API_KEY')
api_secret = config.get('BINANCE', 'SECRET_KEY')

client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()
i = 0
# print(exchange_info)
for s in exchange_info['symbols']:
    print(s['symbol'])
    i += 1

print("tickers in system:" + str(i))
