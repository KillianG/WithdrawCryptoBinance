from BINANCE import BINANCE_API_KEY, BINANCE_API_SECRET
from binance.client import Client
from binance.exceptions import BinanceAPIException

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def withdraw_btc():
    try:
        btc_amount_available = client.get_asset_balance(asset='BTC')['free']
        result = client.withdraw(
            coin='BTC',
            address='bc1qqryehsp4l0jdp5wjsspye9eyqvrtengj7e3404',
            amount=btc_amount_available)
    except BinanceAPIException as e:
        print(e)
    else:
        print("Success")

def withdraw_eth():
    try:
        eth_amount_available = client.get_asset_balance(asset='ETH')['free']
        result = client.withdraw(
            coin='ETH',
            address='0x973E32932b794263C96449CE9bCdCd103294449f',
            amount=eth_amount_available)
    except BinanceAPIException as e:
        print(e)
    else:
        print("Success")


if __name__ == '__main__':
    withdraw_btc()
    withdraw_eth()
