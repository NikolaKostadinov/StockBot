import bravotime, numpy as np, json
from termcolor import colored

def Spec(dataArray, ticker, id):
    
    """Speculate how an array will evolve"""
    
    # Checker
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    #if type(id) is not int: raise TypeError("StockBot Speculate Module: Input should be an integer")
    
    # Parameters
    height0 = len(dataArray)
    
    height = [2, 2]
    layers = len(height)
    
    # Load A.I. Data
    data = json.load(open("ai.json"))[ticker][id]
    
    w, b = [], []
    for key in data:
        w.append(np.matrix(data[key]["w"]))
        b.append(np.array(data[key]["b"]))
    
    firstIter = np.matmul(w[0], dataArray) + b[0]
    secondIter = np.matmul(w[1], firstIter) + b[1]
    
    specArray = secondIter
    
    # Return Values
    now = bravotime.NowString()
    print(colored(f"<{now}| Speculation for {ticker}<{id}> is ready", "green"))
    return specArray