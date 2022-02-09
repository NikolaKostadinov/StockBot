import bravotime, json, nmath
from neuralnetwork import *
from termcolor import colored

def Spec(dataArray, ticker, id):
    
    """Speculate how an array will evolve with provided ticker and id"""
    
    # Checker
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    
    # Set Input Data for A.I.
    L = [1, 3, 9, 9, 3, 1/24]
    L = [int(len(dataArray) * l) for l in L]
    
    W = None # Depends on <ai.json>
    
    X = np.array(dataArray)
    N = np.maximum(X)
    X = nmath.sigmoid(X / N)
    
    # A.I.
    AI = NeuralNetwork(L)
    AI.ImportWeight(W)
    specArray = (N * nmath.logit(AI.Forward(X))).tolist()
    
    # Return Values
    now = bravotime.NowString()
    print(colored(f"<{now}| Speculation for {ticker}<{id}> is ready", "green"))
    return specArray