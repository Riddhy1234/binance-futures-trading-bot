# Binance Futures Testnet Trading Bot

Python CLI bot to place MARKET and LIMIT orders on Binance USDT-M Futures Testnet.

## Setup

1. Create Binance Futures Testnet account and API keys.
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set API keys:

Windows PowerShell:
```bash
setx BINANCE_API_KEY "your_api_key"
setx BINANCE_API_SECRET "your_api_secret"
```

Mac/Linux:
```bash
export BINANCE_API_KEY="your_api_key"
export BINANCE_API_SECRET="your_api_secret"
```

## Run examples

MARKET order:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

LIMIT order:
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Assumptions

- Uses Binance Futures Testnet base URL: `https://testnet.binancefuture.com`
- LIMIT orders use `timeInForce=GTC`
- Logs are saved in `logs/trading_bot.log`
