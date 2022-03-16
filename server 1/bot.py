import json
import bravotime
import os
from security import *
from termcolor import colored

# Start
now = bravotime.NowString()
print(colored("======================================", "blue"))
print(colored(f"<{now}| StockBot is running", "yellow"))

# Get Stocks
tickers = json.load(open("request.json"))["tickers"]

_startTime = bravotime.Now()
security = [Security(ticker=tick, days=240) for tick in tickers]
security = list(map(lambda x: x.SpeculateUpdate(), security))

# Save Data as JSON
data = {secure.ticker: secure.Dict() for secure in security}
jsonString = json.dumps(data, indent=4)
with open("data.json", "w") as file: file.write(jsonString)

# Send Data to Server 0
fileForTransfer = "data.json"
toInstance = "instance-stockbot-0"
zone = "europe-west6-a"

os.system(f"gcloud compute scp {fileForTransfer} --zone={zone} {toInstance}:~/infoData")

now = bravotime.NowString()
print(colored(f"<{now}| Data uploaded to <{toInstance}>", "green"))

# Console Feedback
now = bravotime.NowString()
deltaTimeTotal = (bravotime.Now() - _startTime).total_seconds()
print(colored(f"<{now}| StockBot is at rest", "yellow"))
print(colored(f"<{now}| Total time: {deltaTimeTotal}", "yellow"))