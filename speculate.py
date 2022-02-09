import bravotime, json, nmath
from neuralnetwork import *
from termcolor import colored

def New(dataArray, ticker, id):
    
    """Generate new instance in ai.json"""
    
    # Checker
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    
    # Set Layers
    L = [1, 3, 9, 9, 3, 1/24]
    L = [int(len(dataArray) * l) for l in L]
    n = len(L)

    # Generate New Weights
    wDict = {"0": None}
    wDict.update({str(index): np.zeros(shape=(L[index-1], L[index])).tolist() for index in range(1, n)})
    
    # Convert to JSON
    newDict = json.load(open("ai.json"))
    newDict.update({ticker: {str(id): wDict}})
    
    jsonString = json.dumps(newDict, indent=4)
    with open("ai.json", "w") as file: file.write(jsonString)

def Spec(dataArray, ticker, id):
    
    """Speculate how an array will evolve with provided ticker and id"""
    
    # Checker
    if type(dataArray) is not list: raise TypeError("StockBot Speculate Module: Input should be a list")
    if type(ticker) is not str: raise TypeError("StockBot Speculate Module: Input should be a string")
    
    # Set Input Data for A.I.
    L = [1, 3, 9, 9, 3, 1/24]
    L = [int(len(dataArray) * l) for l in L]
    
    try: json.load(open("ai.json"))[ticker][id]
    except KeyError: New(dataArray, ticker, id)
    
    weightData = json.load(open("ai.json"))[ticker][str(id)]
    W = [None for _ in weightData]
    for index in weightData:
        W[int(index)] = np.array(weightData[index])
    
    X = np.array(dataArray)
    N = np.amax(X, axis=0)
    X = nmath.sigmoid(X / N)
    
    # A.I.
    AI = NeuralNetwork(L)
    AI.ImportWeight(W)
    specArray = (N * nmath.logit(AI.Forward(X))).tolist()
    
    # Return Values
    now = bravotime.NowString()
    print(colored(f"<{now}| Speculation for {ticker}<{id}> is ready", "green"))
    return specArray