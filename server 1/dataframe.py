import yfinance, datetime as t
from business_duration import businessDuration
from dateutil.relativedelta import relativedelta

def DownloadY(downloadable, days, marketSleep):
    
    """Download Yahoo Finance dataframe for ticker"""
    
    now = t.datetime.now()
    before = t.datetime.now() - relativedelta(days=days)
    
    dateFinal = f"{now.year}-{now.month}-{now.day}"
    dateInitial = f"{before.year}-{before.month}-{before.day}"
    
    if marketSleep is False:
        return yfinance.download(
        tickers = downloadable,
        start = dateInitial,
        end = dateFinal,
        interval = "1d",
        progress = False
        ).loc[dateInitial:dateFinal]
    else:
        busy = businessDuration(startdate=before, enddate=now, unit="day")
        DownloadY(downloadable, int(days + busy), False)

def DownloadYDate(downloadable, days, date, marketSleep):
    
    """Download Yahoo Finance dataframe for ticker by date"""
    
    before = date - relativedelta(days=days)
    
    dateFinal = f"{date.year}-{date.month}-{date.day}"
    dateInitial =  f"{before.year}-{before.month}-{before.day}"
    
    if marketSleep is False:
        return yfinance.download(
        tickers = downloadable,
        start = dateInitial,
        end = dateFinal,
        interval = "1d",
        progress = False
        ).loc[dateInitial:dateFinal]
    else:
        busy = businessDuration(startdate=before, enddate=date, unit="day")
        DownloadYDate(downloadable, int(days + busy), date, False)