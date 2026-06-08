VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}

def validate_order(symbol: str, side: str, order_type: str, quantity: float, price: float | None):
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()

    if not symbol.endswith("USDT"):
        raise ValueError("Symbol should be a USDT-M pair, e.g., BTCUSDT")

    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT order")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return symbol, side, order_type
