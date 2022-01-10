from stock import *
import json

# Get Stocks
request = json.load(open("request.json"))
tickers = request["tickers"]
stocks = [Stock(tick) for tick in tickers]

# Save Data as JSON
jsonString = json.dumps({stock.ticker: stock.dictionary for stock in stocks}, indent=4)
with open("data.json", "w") as file: file.write(jsonString)