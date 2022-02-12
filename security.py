import yfinance.shared as shared, datetime as t, bravotime, dataframe, json
from speculate import *
from termcolor import colored

class Security:
    def __init__(self, **kwargs):
        
        """Initiate a Security (Stock / Crypto) object"""
        
        # Checker 1
        if "ticker" in kwargs.keys(): _ticker = kwargs["ticker"]
        else: raise TypeError("StockBot: No ticker input")
        
        # Checker 2
        if type(_ticker) is str: self.ticker = _ticker
        else: raise TypeError("StockBot: Ticker type shoud be a string value")
        
        # Checker 3
        if len(self.ticker) > 5: raise TypeError("StockBot: Ticker has too many letters")
        elif len(self.ticker) < 1: raise TypeError("StockBot: Ticker has not enough letters")
        
        # Checker 4
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
        
        # Set Date And Get Security Data
        if "date" in kwargs:
            date = kwargs["date"]
            
            if json.load(open("information.json"))[self.ticker]["market"] == "crypto":
                self.dataframe = dataframe.DownloadDate(self.ticker + "-USD", date)
            else: self.dataframe = dataframe.DownloadDate(self.ticker, date)
            if shared._ERRORS: raise TypeError("StockBot: Ticker not found")
            
            self.now = bravotime.Convert(date)
        else:
            if json.load(open("information.json"))[self.ticker]["market"] == "crypto":
                self.dataframe = dataframe.Download(self.ticker + "-USD")
            else: self.dataframe = dataframe.Download(self.ticker)
            if shared._ERRORS: raise TypeError("StockBot: Ticker not found")
            
            self.now = bravotime.Now()
        
        # Get Security Data
        if json.load(open("information.json"))[self.ticker]["market"] == "crypto":
            self.dataframe = dataframe.Download(self.ticker + "-USD")
        else: self.dataframe = dataframe.Download(self.ticker)
        if shared._ERRORS: raise TypeError("StockBot: Ticker not found")
        
        # Save Security Data
        self.openValues = self.dataframe["Open"].to_list()
        self.closeValues = self.dataframe["Close"].to_list()
        self.highValues = self.dataframe["High"].to_list()
        self.lowValues = self.dataframe["Low"].to_list()
        
        if len(self.openValues) == len(self.closeValues) == len(self.highValues) == len(self.lowValues): self.length = len(self.highValues)
        else: raise ValueError("StockBot: Missing data")
        
        # Rate of Change
        self.openRate = [0 for _ in range(self.length)]
        for index in range(1, self.length):
            self.openRate[index] = self.openValues[index] - self.openValues[index-1]
            
        self.closeRate = [0 for _ in range(self.length)]
        for index in range(1, self.length):
            self.closeRate[index] = self.closeValues[index] - self.closeValues[index-1]
            
        self.highRate = [0 for _ in range(self.length)]
        for index in range(1, self.length):
            self.highRate[index] = self.highValues[index] - self.highValues[index-1]
            
        self.lowRate = [0 for _ in range(self.length)]
        for index in range(1, self.length):
            self.lowRate[index] = self.lowValues[index] - self.lowValues[index-1]
        
        # Time
        self.minuteNow = self.now.minute
        self.hourNow = self.now.hour
        self.dayNow = self.now.day
        self.monthNow = self.now.month
        self.yearNow = self.now.year
        
        # Console Feedback
        now = bravotime.NowString()
        print(colored(f"<{now}| {self.ticker} data successfully loaded", "green"))
    
        # Vulyo Magic
        self._createdOn = 1617194210928

    def SpeculatePotential(self):
        
        """"""
        
        return [Pot(self.openRate), Pot(self.closeRate), Pot(self.highRate), Pot(self.lowRate)]

    def SpeculateUpdate(self):
        
        """"""
        
        # A.I.
        self.openMoment = Spec(self.openRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker}<open> is ready", "green"))
        
        self.closeMoment = Spec(self.closeRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker}<close> is ready", "green"))
        
        self.highMoment = Spec(self.highRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker}<high> is ready", "green"))
        
        self.lowMoment = Spec(self.lowRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker}<low> is ready", "green"))
        
        # Return New Values
        self.openSpec = [0 for _, _ in enumerate(self.openMoment)]
        self.openSpec[0] = self.openMoment[0] + self.openValues[-1]
        for index, this in enumerate(self.openMoment):
            self.openSpec[index] = self.openSpec[index-1] + this
            
        self.closeSpec = [0 for _, _ in enumerate(self.closeMoment)]
        self.closeSpec[0] = self.closeMoment[0] + self.closeValues[-1]
        for index, this in enumerate(self.closeMoment):
            self.closeSpec[index] = self.closeSpec[index-1] + this
            
        self.highSpec = [0 for _, _ in enumerate(self.highMoment)]
        self.highSpec[0] = self.highMoment[0] + self.highValues[-1]
        for index, this in enumerate(self.highMoment):
            self.highSpec[index] = self.highSpec[index-1] + this
            
        self.lowSpec = [0 for _, _ in enumerate(self.lowMoment)]
        self.lowSpec[0] = self.lowMoment[0] + self.lowValues[-1]
        for index, this in enumerate(self.lowMoment):
            self.lowSpec[index] = self.lowSpec[index-1] + this
        
        if len(self.openSpec) == len(self.closeSpec) == len(self.highSpec) == len(self.lowSpec): pass
        else: raise ValueError("StockBot: Missing data")
        
        return self

    def Print(self): print(self.dataframe)
    
    def Dict(self):
        
        """Return __dict__ without object valued attributes"""
        
        dict = self.__dict__
        del dict["now"], dict["dataframe"]
        return dict