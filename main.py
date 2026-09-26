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