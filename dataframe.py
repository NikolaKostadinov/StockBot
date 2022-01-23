import yfinance

def download(downloadable): return yfinance.download(tickers=downloadable, period="1d", interval="15m", progress=False)