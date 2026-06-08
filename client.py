import time
import hmac
import hashlib
import os
from urllib.parse import urlencode

import requests


class BinanceFuturesClient:
    def __init__(self, logger):
        self.base_url = "https://testnet.binancefuture.com"
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.logger = logger

        if not self.api_key or not self.api_secret:
            raise ValueError("Missing BINANCE_API_KEY or BINANCE_API_SECRET environment variables")

    def _sign(self, params: dict) -> str:
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def _request(self, method: str, endpoint: str, params: dict):
        params["timestamp"] = int(time.time() * 1000)
        params["signature"] = self._sign(params)

        headers = {"X-MBX-APIKEY": self.api_key}
        url = self.base_url + endpoint

        self.logger.info("API Request: %s %s params=%s", method, endpoint, params)

        try:
            response = requests.request(method, url, headers=headers, params=params, timeout=10)
            data = response.json()
            self.logger.info("API Response: status=%s body=%s", response.status_code, data)

            if response.status_code >= 400:
                raise Exception(f"Binance API Error: {data}")

            return data

        except requests.exceptions.RequestException as e:
            self.logger.error("Network error: %s", str(e))
            raise Exception(f"Network error: {e}")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float | None = None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self._request("POST", "/fapi/v1/order", params)
