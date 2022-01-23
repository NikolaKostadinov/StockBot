import yfinance

def download(downloadable): return yfinance.download(tickers=downloadable, period="3mo", interval="1m", progress=False)