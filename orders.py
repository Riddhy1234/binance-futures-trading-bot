from bot.validators import validate_order

def place_validated_order(client, symbol, side, order_type, quantity, price=None):
    symbol, side, order_type = validate_order(symbol, side, order_type, quantity, price)
    return client.place_order(symbol, side, order_type, quantity, price)
