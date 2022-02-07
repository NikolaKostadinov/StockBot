import bravotime, json
from termcolor import colored

def Spec(dataArray, ticker, id):
    
    """Speculate how an array will evolve with provided ticker and id"""
    
    # Checker
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    
    specArray = None
    
    # Return Values
    now = bravotime.NowString()
    print(colored(f"<{now}| Speculation for {ticker}<{id}> is ready", "green"))
    return specArray