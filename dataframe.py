import yfinance

def Download(downloadable): return yfinance.download(tickers=downloadable, period="1y", interval="1d", progress=False)