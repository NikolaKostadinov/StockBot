from stock import *
import datetime as t
import json

# Get Stocks
request = json.load(open("request.json"))
tickers = request["tickers"]

_startTime = t.datetime.now()
stocks = [Stock(tick) for tick in tickers]
deltaTimeTotal = (t.datetime.now() - _startTime).total_seconds()
del _startTime

# Save Data as JSON
data = {stock.ticker: stock.Dict() for stock in stocks}
data.update({"deltaTimeTotal": deltaTimeTotal})
jsonString = json.dumps(data, indent=4)
with open("data.json", "w") as file: file.write(jsonString)