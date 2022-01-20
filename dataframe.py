import yfinance

def download(downloadable): return yfinance.download(tickers=downloadable, period="3h", interval="15m")