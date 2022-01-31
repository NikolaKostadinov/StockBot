import datetime as t
from security import *
from termcolor import colored
import numpy as np

def Speculate(dataArray, ticker, id):
    
    """Speculate how an array will evolve"""
    
    # Checker
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    if type(id) is not int: raise TypeError("StockBot Speculate Module: Input should be an integer")
    
    # Parameters
    height0 = len(dataArray)
    
    height = [height0, height0+2, height0+2, height0, height0//24]
    layers = len(height)
    
    # Load A.I. Data
    data = json.load(open("ai.json"))[ticker][id]
    
    w, b = [], []
    for layer in range(layers):
        w.append(np.matrix(data[layer]["w"]))
        b.append(np.array(data[layer]["b"]))
        
    print(w[0], b[0])
    
    specArray = None
    
    # Return Values
    now = t.datetime.now().strftime("%H:%M")
    print(colored(f"<{now}| Speculation for {ticker}<{id}> is ready", "green"))
    return specArray