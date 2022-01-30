from security import *
import datetime as t
import json

# Get Stocks
tickers = ["TSLA", "ETH"]
_startTime = t.datetime.now()
security = [Security(tick) for tick in tickers]

# Save Data as JSON
data = {this.ticker: this.Dict() for this in security}
deltaTimeTotal = (t.datetime.now() - _startTime).total_seconds()
del _startTime
data.update({"deltaTimeTotal": deltaTimeTotal})
jsonString = json.dumps(data, indent=4)
with open("data.json", "w") as file: file.write(jsonString)

now = t.datetime.now().strftime("%H:%M")
print(f"<{now}| StockBot is at rest")
print(f"<{now}| Total time: {deltaTimeTotal}")