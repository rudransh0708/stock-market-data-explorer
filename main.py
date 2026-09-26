import yfinance as yf
stock = yf.Ticker("AAPL")
data = stock.history(period="5d")
print(data.to_string())