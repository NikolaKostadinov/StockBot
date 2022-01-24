from security import *
import datetime as t
import json

# Get Stocks
request = json.load(open("request.json"))
tickers = request["tickers"]

_startTime = t.datetime.now()
security = [Security(tick) for tick in tickers]

# Save Data as JSON
data = {this.ticker: this.Dict() for this in security}
deltaTimeTotal = (t.datetime.now() - _startTime).total_seconds()
del _startTime
data.update({"deltaTimeTotal": deltaTimeTotal})
jsonString = json.dumps(data, indent=4)
with open("data.json", "w") as file: file.write(jsonString)

print("StockBot is at rest")
print(deltaTimeTotal)