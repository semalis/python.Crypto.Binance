import shrimpy

import configparser
# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('../secret.cfg'))
api_key = config.get('BINANCE', 'API_KEY')
api_secret = config.get('BINANCE', 'SECRET_KEY')


# This is a sample handler, it simply prints the incoming message to the console
def error_handler(err):
    print(err)


# This is a sample handler, it simply prints the incoming message to the console
def handler(msg):
    print(msg)


api_client = shrimpy.ShrimpyApiClient(api_key, api_secret)
raw_token = api_client.get_token()
client = shrimpy.ShrimpyWsClient(error_handler, raw_token['token'])

subscribe_data = {
    "type": "subscribe",
    "exchange": "coinbasepro",
    "pair": "ltc-btc",
    "channel": "orderbook"
}

# Start processing the Shrimpy websocket stream!
client.connect()
client.subscribe(subscribe_data, handler)

# Once complete, stop the client
client.disconnect()