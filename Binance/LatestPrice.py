# https://algotrading101.com/learn/binance-python-api-guide/

from binance.client import Client

import configparser

import logging
from binance import Client
# from binance.lib.utils import config_logging
# from binance.error import ClientError

# Загрузка ключей из файла config
config = configparser.ConfigParser()
config.read_file(open('../secret.cfg'))
api_key = config.get('BINANCE', 'API_KEY')
api_secret = config.get('BINANCE', 'SECRET_KEY')

# import binance

# binance.client
# binance.balances()
# config_logging(logging, logging.DEBUG)


client = Client(api_key, api_secret)
print(client.get_deposit_history())
# try:
# response = client.get_c2c_trade_history() #.get_recent_trades(symbol="BTCUSDT") #.get_account_trades(symbol = "BTCUSDT", recvWindow=6000)
# print(response)
# except ClientError as error:
#     logging.error(
#         "Found error. status: {}, error code: {}, error message: {}".format(
#             error.status_code, error.error_code, error.error_message
#         )
#     )


# client = Client(api_key, api_secret)

# get latest price from Binance API
# btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
# print full output (dictionary)
# print(btc_price)

# print(btc_price["price"])
# get all symbol prices
# prices = client.get_all_tickers()
# print(prices)
# fetch list of withdrawals
# from binance.exceptions import BinanceAPIException
# try:
#     result = client.withdraw(
#         asset='ETH',
#         address='<eth_address>',
#         amount=100)
# except BinanceAPIException as e:
#     print(e)
# else:
#     print("Success")
#
# # fetch list of withdrawals
# withdraws = client.get_withdraw_history()
# print(withdraws)
# this would result in verify: False and timeout: 5 for the get_all_orders call
# client = Client(api_key, api_secret, {"verify": False, "timeout": 20})
# client.get_all_orders(symbol='BNBBTC', requests_params={'timeout': 5})