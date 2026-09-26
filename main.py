import yfinance as yf

tickers = ["AAPL", "MSFT", "NVDA", "JPM", "TSLA", "AMZN"]

data = yf.download(
    tickers,
    period="5y",
    interval="1d",
    auto_adjust=True
)

close_prices = data["Close"]

print(close_prices.head())

aapl = close_prices["AAPL"]

day_1 = aapl.iloc[0]
day_2 = aapl.iloc[1]

daily_return = (day_2 - day_1) / day_1

print(f"Day 1 close: ${day_1:.2f}")
print(f"Day 2 close: ${day_2:.2f}")
print(f"AAPL daily return: {daily_return * 100:.2f}%")

daily_returns = close_prices.pct_change()

print(daily_returns.head())

# Cumulative returns
cumulative_returns = (1 + daily_returns).cumprod() - 1

print("\nCumulative returns:")
print(cumulative_returns.head())

print("\nTotal cumulative returns:")
print(cumulative_returns.iloc[-1] * 100)