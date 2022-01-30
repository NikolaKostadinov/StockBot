import yfinance

def download(downloadable): return yfinance.download(tickers=downloadable, period="1d", interval="5m", progress=False)