import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_validated_order
from bot.logging_config import setup_logger


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair, e.g., BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT order")

    args = parser.parse_args()
    logger = setup_logger()

    print("\nOrder Request Summary")
    print("---------------------")
    print(f"Symbol   : {args.symbol.upper()}")
    print(f"Side     : {args.side.upper()}")
    print(f"Type     : {args.type.upper()}")
    print(f"Quantity : {args.quantity}")
    if args.price:
        print(f"Price    : {args.price}")

    try:
        client = BinanceFuturesClient(logger)

        response = place_validated_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\nOrder Response Details")
        print("----------------------")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
        print("\nSUCCESS: Order placed successfully.")

    except Exception as e:
        logger.error("Order failed: %s", str(e))
        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()
