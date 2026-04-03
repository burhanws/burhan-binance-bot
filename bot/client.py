import os
from dotenv import load_dotenv
from binance.client import Client
load_dotenv()
class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        if not api_key or not api_secret:
            raise RuntimeError("Missing BINANCE_API_KEY or BINANCE_API_SECRET")
        self.client = Client(api_key, api_secret, testnet=True)
    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {"symbol": symbol, "side": side, "type": order_type, "quantity": quantity}
        if order_type == "LIMIT":
            params["timeInForce"] = "GTC"
            params["price"] = price
        return self.client.futures_create_order(**params)
