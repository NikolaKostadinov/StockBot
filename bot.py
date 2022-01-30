from security import *
from termcolor import colored
import datetime as t
import json

# Start
now = t.datetime.now().strftime("%H:%M")
print(colored(f"<{now}| StockBot is running", "yellow"))

# Get Stocks
tickers = json.load(open("request.json"))["tickers"]

_startTime = t.datetime.now()
security = [Security(tick) for tick in tickers]

# Save Data as JSON
data = {this.ticker: this.Dict() for this in security}
deltaTimeTotal = (t.datetime.now() - _startTime).total_seconds()
del _startTime
data.update({"deltaTimeTotal": deltaTimeTotal})
jsonString = json.dumps(data, indent=4)
with open("data.json", "w") as file: file.write(jsonString)

# Console Feedback
now = t.datetime.now().strftime("%H:%M")
print(colored(f"<{now}| StockBot is at rest", "blue"))
print(colored(f"<{now}| Total time: {deltaTimeTotal}", "blue"))