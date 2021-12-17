from binance.client import Client

import configparser

# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('../secret.cfg'))
api_key = config.get('BINANCE', 'API_KEY')
api_secret = config.get('BINANCE', 'SECRET_KEY')

client = Client(api_key, api_secret)
exchange_info = client.get_exchange_info()
# for s in exchange_info['symbols']:
#     print(s['symbol'])

from time import sleep
from binance import ThreadedWebsocketManager

btc_price = {'error': False}


def btc_trade_history(msg):
    """ define how to process incoming WebSocket messages """
    if msg['e'] != 'error':
        print("Ticker: " + msg['s'] + " close:" + msg['c'] + " change %:" + msg['p'])
        btc_price['last'] = msg['c']
        btc_price['ticker'] = msg['s']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
        btc_price['percent'] = msg['p']
        btc_price['error'] = False
    else:
        btc_price['error'] = True


# init and start the WebSocket


bsm = ThreadedWebsocketManager()
bsm.start()

# subscribe to a stream

for s in exchange_info['symbols']:
    # print(s['symbol'])
    bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol=s['symbol'])
