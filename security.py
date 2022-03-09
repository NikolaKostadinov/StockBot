import yfinance.shared as shared
import bravotime
import dataframe
import json
from speculate import *
from termcolor import colored

class Security:
    def __init__(self, **kwargs):
        
        """Initiate a Security (Stock / Crypto) object"""
        
        # Checker 1
        if "ticker" in kwargs: _ticker = kwargs["ticker"]
        else: raise TypeError(colored("StockBot: No ticker input", "red"))

        # Checker 2
        if "days" in kwargs: _days = kwargs["days"]
        else: raise TypeError(colored("StockBot: No time input", "red"))
        
        # Checker 3
        if type(_ticker) is str: self.ticker = _ticker
        else: raise TypeError(colored("StockBot: Ticker type should be a string value", "red"))

        # Checker 4
        if type(_days) is int: self.length = _days
        else: raise TypeError(colored("StockBot: Days type should be an int value", "red"))
        
        # Checker 5
        if len(self.ticker) > 5: raise TypeError(colored("StockBot: Ticker has too many letters", "red"))
        elif len(self.ticker) < 1: raise TypeError(colored("StockBot: Ticker has not enough letters", "red"))

        # Checker 6
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
                self.dataframe = dataframe.DownloadYDate(self.ticker + "-USD", self.length, date, False)
            else: self.dataframe = dataframe.DownloadYDate(self.ticker, self.length, date, True)
            if shared._ERRORS:raise TypeError("StockBot: Ticker not found")

            self.now = bravotime.Convert(date)
        else:
            if json.load(open("information.json"))[self.ticker]["market"] == "crypto":
                self.dataframe = dataframe.DownloadY(self.ticker + "-USD", self.length, False)
            else: self.dataframe = dataframe.DownloadY(self.ticker, self.length, True)
            if shared._ERRORS: raise TypeError("StockBot: Ticker not found")

            self.now = bravotime.Now()

        # Save Security Data
        self.openValues = self.dataframe["Open"].to_list()
        self.closeValues = self.dataframe["Close"].to_list()
        self.highValues = self.dataframe["High"].to_list()
        self.lowValues = self.dataframe["Low"].to_list()

        if len(self.openValues) == len(self.closeValues) == len(self.highValues) == len(self.lowValues) == self.length: pass
        else:
            diff = abs(self.length - len(self.openValues))
            raise ValueError(colored(f"StockBot: Missing data. Difference of {diff}", "red"))

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
        
    def SpeculateUpdate(self):
        
        """Append seculated values"""

        # A.I.
        self.openMoment = Spec(self.openRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker} <open> is ready", "green"))

        self.closeMoment = Spec(self.closeRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker} <close> is ready", "green"))

        self.highMoment = Spec(self.highRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker} <high> is ready", "green"))

        self.lowMoment = Spec(self.lowRate)
        now = bravotime.NowString()
        print(colored(f"<{now}| Speculation for {self.ticker} <low> is ready", "green"))

        # Return New Values
        self.openSpec = [0 for _, _ in enumerate(self.openMoment)]
        self.openSpec[0] = self.openMoment[0] + self.openValues[-1]
        for index, this in enumerate(self.openMoment):
            if index != 0: self.openSpec[index] = self.openSpec[index-1] + this

        self.closeSpec = [0 for _, _ in enumerate(self.closeMoment)]
        self.closeSpec[0] = self.closeMoment[0] + self.closeValues[-1]
        for index, this in enumerate(self.closeMoment):
            if index != 0: self.closeSpec[index] = self.closeSpec[index-1] + this

        self.highSpec = [0 for _, _ in enumerate(self.highMoment)]
        self.highSpec[0] = self.highMoment[0] + self.highValues[-1]
        for index, this in enumerate(self.highMoment):
            if index != 0: self.highSpec[index] = self.highSpec[index-1] + this

        self.lowSpec = [0 for _, _ in enumerate(self.lowMoment)]
        self.lowSpec[0] = self.lowMoment[0] + self.lowValues[-1]
        for index, this in enumerate(self.lowMoment):
            if index != 0: self.lowSpec[index] = self.lowSpec[index-1] + this

        if len(self.openSpec) == len(self.closeSpec) == len(self.highSpec) == len(self.lowSpec): pass
        else: raise ValueError(colored("StockBot: Missing data", "red"))

        return self

    def Print(self): print(self.dataframe)

    def Dict(self):
        
        """Return __dict__ without object valued attributes"""

        dict = self.__dict__
        del dict["now"], dict["dataframe"]
        
        return dict
