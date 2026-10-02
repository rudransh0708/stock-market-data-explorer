import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "NVDA", "JPM", "TSLA", "AMZN"]

data = yf.download(
    tickers,
    period="5y",
    interval="1d",
    auto_adjust=True
)

close_prices = data["Close"]

print(close_prices.head())


# AAPL closing prices
aapl = close_prices["AAPL"]


# Manually calculate one daily return
day_1 = aapl.iloc[0]
day_2 = aapl.iloc[1]

daily_return = (day_2 - day_1) / day_1

print(f"Day 1 close: ${day_1:.2f}")
print(f"Day 2 close: ${day_2:.2f}")
print(f"AAPL daily return: {daily_return * 100:.2f}%")


# Daily returns for all stocks
daily_returns = close_prices.pct_change()

print("\nDaily returns:")
print(daily_returns.head())

# Volatility
daily_volatility = daily_returns.std()

annualized_volatility = daily_volatility * (252 ** 0.5)

print("\nDaily volatility:")
print(daily_volatility * 100)

print("\nAnnualized volatility:")
print(annualized_volatility * 100)

# Maximum drawdown
running_peak = close_prices.cummax()

drawdowns = (close_prices / running_peak) - 1

max_drawdown = drawdowns.min()

print("\nMaximum drawdown:")
print(max_drawdown * 100)


# Cumulative returns
cumulative_returns = (1 + daily_returns).cumprod() - 1

print("\nCumulative returns:")
print(cumulative_returns.head())

print("\nTotal cumulative returns:")
print(cumulative_returns.iloc[-1] * 100)


# Moving averages for AAPL
ma_20 = aapl.rolling(window=20).mean()
ma_50 = aapl.rolling(window=50).mean()


# Plot cumulative returns
(cumulative_returns * 100).plot(figsize=(12, 6))

plt.title("Cumulative Returns Over 5 Years")
plt.xlabel("Date")
plt.ylabel("Cumulative Return (%)")
plt.legend(title="Ticker")
plt.grid(True)
plt.tight_layout()

plt.savefig("figures/cumulative_returns.png", dpi=300)
plt.show()


# Plot AAPL price and moving averages
plt.figure(figsize=(12, 6))

plt.plot(aapl, label="AAPL Price")
plt.plot(ma_20, label="20-Day Moving Average")
plt.plot(ma_50, label="50-Day Moving Average")

plt.title("AAPL Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("figures/aapl_moving_averages.png", dpi=300)
plt.show()

# Plot annualized volatility
plt.figure(figsize=(10, 6))

(annualized_volatility * 100).plot(kind="bar")

plt.title("Annualized Volatility")
plt.xlabel("Stock")
plt.ylabel("Volatility (%)")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("figures/annualized_volatility.png", dpi=300)
plt.show()

# Plot maximum drawdown
plt.figure(figsize=(10, 6))

(max_drawdown * 100).plot(kind="bar")

plt.title("Maximum Drawdown Over 5 Years")
plt.xlabel("Stock")
plt.ylabel("Maximum Drawdown (%)")
plt.grid(axis="y")
plt.tight_layout()

plt.savefig("figures/maximum_drawdown.png", dpi=300)
plt.show()