import yfinance, datetime as t

def Download(downloadable):
    
    """Download Yahoo Finance dataframe for ticker"""
    
    return yfinance.download(
    tickers = downloadable,
    period = "1y",
    interval = "1d",
    progress = False
    )

def DownloadDate(downloadable, date):
    
    """Download Yahoo Finance dataframe for ticker by date"""
    
    dateFinl = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    dateInit =  str(date.year - 1) + "-" + str(date.month) + "-" + str(date.day)
    
    return yfinance.download(
    tickers = downloadable,
    start = dateInit,
    end = dateFinl,
    interval = "1d",
    progress = False
    )