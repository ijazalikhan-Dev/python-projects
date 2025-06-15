from binance.client import Client
import statistics

# Binance se data lelo (BTC/USDT 1-hour)
client = Client()
klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 year ago UTC")

close_prices = [float(candle[4]) for candle in klines]  # Close prices list

capital = 1000  # Starting USDT
holding_usdt = True  # Start with USDT
trades = []  # Trade history

for i in range(20, len(close_prices)):
    last_20_prices = close_prices[i - 20:i]
    sma = statistics.mean(last_20_prices)
    std_dev = statistics.stdev(last_20_prices)

    upper_band = sma + 2 * std_dev
    lower_band = sma - 2 * std_dev

    current_price = close_prices[i]

    if holding_usdt and current_price < lower_band:
        # BUY BTC (USDT se)
        btc_amount = capital / current_price
        capital = 0
        holding_usdt = False
        trades.append(("BUY", current_price, i))

    elif not holding_usdt and current_price > upper_band:
        # SELL BTC (USDT mein)
        capital = btc_amount * current_price
        holding_usdt = True
        trades.append(("SELL", current_price, i))

# Final Result
print("Total Trades:", len(trades))
print("Final Capital:", capital, "USDT")
print("Trade History:",trades)
