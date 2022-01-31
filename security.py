import yfinance.shared as shared, datetime as t, dataframe, json
from speculate import *
from termcolor import colored

class Security:
    def __init__(self, _ticker):
        
        """Initiate a Security (Stock / Crypto) object"""
        
        # Checker 1
        if type(_ticker) is str: self.ticker = _ticker
        else: raise TypeError("StockBot: Ticker type shoud be a string value")
        
        # Checker 2
        try: json.load(open("information.json"))[self.ticker]
        except KeyError:
            print(colored(f"No information for {self.ticker} in information.json", "red"))
            data = json.load(open("information.json"))
            
            nullInfo = {
                "name": None,
                "ceo": None,
                "headquarters": None,
                "market": None,
                "description": None
            }
            
            data[self.ticker] = nullInfo
            jsonString = json.dumps(data, indent=4)
            with open("information.json", "w") as file: file.write(jsonString)
        
        # Get Stock Data
        if json.load(open("information.json"))[self.ticker]["market"] == "crypto":
            self.now = t.datetime.now()
            self.dataframe = dataframe.Download(self.ticker + "-USD")
        else:
            self.now = t.datetime.now()
            self.dataframe = dataframe.Download(self.ticker)
        if shared._ERRORS: raise TypeError("StockBot: Ticker not found")
        
        # Save Stock Data
        self.openValues = self.dataframe["Open"].to_list()
        self.closeValues = self.dataframe["Close"].to_list()
        self.highValues = self.dataframe["High"].to_list()
        self.lowValues = self.dataframe["Low"].to_list()
        
        if len(self.openValues) == len(self.closeValues) == len(self.highValues) == len(self.lowValues): self.length = len(self.highValues)
        else: raise ValueError("StockBot: Missing data")
        
        # A.I.
        self.openSpec = Speculate(self.openValues)
        self.closeSpec = Speculate(self.closeValues)
        self.highSpec = Speculate(self.highValues)
        self.lowSpec = Speculate(self.lowValues)
        
        # Time
        self.deltaTime = (t.datetime.now() - self.now).total_seconds()
        self.minuteNow = self.now.minute
        self.hourNow = self.now.hour
        self.dayNow = self.now.day
        self.monthNow = self.now.month
        self.yearNow = self.now.year
        now = t.datetime.now().strftime("%H:%M")
        
        # Console Feedback
        print(colored(f"<{now}| {self.ticker} data successfully loaded", "green"))
    
    def Print(self): print(self.dataframe)
    
    def Dict(self):
        
        """Return __dict__ without object valued attributes"""
        
        dict = self.__dict__
        del dict["now"], dict["dataframe"]
        return dict