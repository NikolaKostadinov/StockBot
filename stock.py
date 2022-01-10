import yfinance
import datetime as t
import json

class Stock:
    def __init__(self, _ticker):
        """Initiate a Stock object"""
        self.ticker = _ticker
        
        # Get Stock Data
        self.now = t.datetime.now()
        self.dataframe = yfinance.download(tickers=self.ticker, period="2h", interval="15m")
        
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
        
        # Save Stock Change
        self.openChange = []
        for index in range(1, len(self.openValues)):
            self.openChange.append(self.openValues[index] - self.openValues[index-1])
        self.closeChange = []
        for index in range(1, len(self.closeValues)):
            self.closeChange.append(self.closeValues[index] - self.closeValues[index-1])
        self.highChange = []
        for index in range(1, len(self.highValues)):
            self.highChange.append(self.highValues[index] - self.highValues[index-1])
        self.lowChange = []
        for index in range(1, len(self.lowValues)):
            self.lowChange.append(self.lowValues[index] - self.lowValues[index-1])
    
    def Print(self): print(self.dataframe)
    
    def ToJSON(self):
        """Save Stock object as a JSON string"""
        dict = self.__dict__
        del dict["now"], dict["dataframe"]
        with open("data.json", "w") as file: file.write(json.dumps(dict, indent=4))