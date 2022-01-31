import datetime as t
from security import *
from termcolor import colored

def Speculate(dataArray, ticker, id):
    
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    if type(id) is not int: raise TypeError("StockBot Speculate Module: Input should be an integer")
    
    # A.I. Blackbox Magic goes here
    specArray = [0]
    
    now = t.datetime.now().strftime("%H:%M")
    print(colored(f"<{now}| Speculation for {ticker}<{id}> is ready", "green"))
    return specArray