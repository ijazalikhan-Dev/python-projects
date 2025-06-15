from binance.client import Client
my_client = Client()
klines = my_client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "30 May, 2024")
print(klines)
for candle in klines:
    print(candle)
    print(candle[:5])
    print(candle[5:])