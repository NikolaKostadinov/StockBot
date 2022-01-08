import yfinance
import datetime as t
import json

class Stock:
    def __init__(self, _ticket):
        """Initiate a Stock object"""
        # Get Stock Data
        self.now = t.datetime.now()
        self.dataframe = yfinance.download(tickers=_ticket, period="2h", interval="15m")
        
        # Time
        self.delat = (t.datetime.now() - self.now).total_seconds()
        self.minuteNow = self.now.minute
        self.hourNow = self.now.hour
        self.dayNow = self.now.day
        self.monthNow = self.now.month
        self.yearNow = self.now.year
        
        # Save Stock Data
        self.openValues = self.dataframe["Open"].to_list()
        self.closeValues = self.dataframe["Close"].to_list()
        self.highValues = self.dataframe["High"].to_list()
        self.lowValues = self.dataframe["Low"].to_list()
        
    def Print(self): print(self.dataframe)

    def toJSON(self):
        """Save Stock object as a JSON string"""
        dict = self.__dict__
        del dict["now"], dict["dataframe"]
        with open("data.json", "w") as file: file.write(json.dumps(dict, indent=4))