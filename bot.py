from yfinance import ticker
from stock import *
import json

# Get Stocks
request = json.load(open("request.json"))
tickers = request["tickers"]
stocks = [Stock(tick) for tick in tickers]

# Save Data as JSON