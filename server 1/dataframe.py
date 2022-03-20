import yfinance, datetime as t
from dateutil.relativedelta import relativedelta

def DownloadYDate(downloadable, days, date, marketSleep):
    
    """Download Yahoo Finance dataframe for ticker by date"""
    
    now = date
    before = now - relativedelta(days=days)
    
    if marketSleep is True:
        before -= relativedelta(days=106) # 106 ONLY WORKS FOR 240 DAYS
        
    dateFinal = f"{now.year}-{now.month}-{now.day}"
    dateInitial = f"{before.year}-{before.month}-{before.day}"
        
    return yfinance.download(
        tickers = downloadable,
        start = dateInitial,
        end = dateFinal,
        interval = "1d",
        progress = False
        ).loc[dateInitial:dateFinal]
    
def DownloadY(downloadable, days, marketSleep):
    
    """Download Yahoo Finance dataframe for ticker"""
    
    return DownloadYDate(downloadable, days, t.datetime.now(), marketSleep)