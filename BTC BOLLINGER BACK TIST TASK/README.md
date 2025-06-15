

📄 README.md

# 📊 BTC Bollinger Backtest

This Python project performs a *backtest on BTC/USDT trading* using *Bollinger Bands. It fetches historical price data from the **Binance API, generates **buy and sell signals*, and calculates the final capital after simulated trading.

---

## 📁 Project Files

- BTC bollinger tist.py: Main backtesting file (generates signals and prints trade history & final capital).
- BTC Price.py: Fetches and prints historical candle data from Binance.
- BTC BUY AND SELL.py: (Optional file, if used for specific logic or plotting buy/sell signals).
- README.md: Project documentation (this file).

---

## ⚙ How to Run

1. Make sure *Python 3.x* is installed.
2. Install required dependencies:

```bash
pip install python-binance

3. Run the backtest script:

python "BTC bollinger tist.py"

📊 Output Includes

Total number of trades executed

Final capital in USDT

Buy and sell trade history with timestamps and prices

📚 Libraries Used

python-binance – for accessing Binance historical data

statistics – for mean and standard deviation

datetime – for handling timeframes


🧠 Data Source

The project fetches 1-hour interval historical price data for the BTC/USDT trading pair from Binance.

👥 Contributors

Mufti Ijaz


📌 Note

This is a backtesting simulation only. It does not execute real trades and is intended for educational and research purposes.

