import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")

hist

data = yf.download("SPY AAPL", period="1mo")
