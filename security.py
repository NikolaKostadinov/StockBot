import yfinance.shared as shared, datetime as t, dataframe

class Security:
    def __init__(self, _ticker):
        """Initiate a Security (Stock / Crypto) object"""
        if type(_ticker) is str: self.ticker = _ticker
        else: raise TypeError("StockBot: Ticker type shoud be a string value")
        
        # Get Stock Data
        self.now = t.datetime.now()
        self.dataframe = dataframe.download(self.ticker)
        if shared._ERRORS:
            self.dataframe = dataframe.download(self.ticker + "-USD")
            if shared._ERRORS: raise TypeError("StockBot: Ticker not found")
            else: self.type = "crypto"
        else: self.type = "stock"
            
        # Time
        self.deltaTime = (t.datetime.now() - self.now).total_seconds()
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
        
        if len(self.openValues) == len(self.closeValues) == len(self.highValues) == len(self.lowValues): self.length = len(self.highValues)
        else: raise ValueError("StockBot: Missing index")
        
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
    
    def Dict(self):
        """Return __dict__ without object valued attributes"""
        dict = self.__dict__
        del dict["now"], dict["dataframe"]
        return dict