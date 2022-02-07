import json, bravotime
from security import *
from termcolor import colored

# Start
now = bravotime.NowString()
print(colored(f"<{now}| StockBot is running", "yellow"))

# Get Stocks
tickers = json.load(open("request.json"))["tickers"]

_startTime = bravotime.Now()
security = [Security(tick) for tick in tickers]

# Save Data as JSON
data = {this.ticker: this.Dict() for this in security}
deltaTimeTotal = (bravotime.Now() - _startTime).total_seconds()
del _startTime
data.update({"deltaTimeTotal": deltaTimeTotal})
jsonString = json.dumps(data, indent=4)
with open("data.json", "w") as file: file.write(jsonString)

# Console Feedback
now = bravotime.NowString()
print(colored(f"<{now}| StockBot is at rest", "blue"))
print(colored(f"<{now}| Total time: {deltaTimeTotal}", "blue"))