import json
import nmath
from neuralnetwork import *

def UpWei(dataArray, weightArray):
    
    """Import weights to ai.json"""

    # Checker
    if type(dataArray) is not list or type(weightArray) is not list:
        raise TypeError("StockBot Speculate Module: Input should be a list")

    # Set Layers
    L = [1, 3, 9, 9, 3, 1/24]
    L = [int(len(dataArray) * l) for l in L]
    n = len(L)

    # Import Weights
    wDict = {str(index): None for index in range(n)}
    for index in range(n):
        if weightArray[index] is None: wDict[str(index)] = None
        else: wDict[str(index)] = weightArray[index].tolist()

    # Convert to JSON
    jsonString = json.dumps(wDict, indent=4)
    with open("ai.json", "w") as file: file.write(jsonString)


def New(dataArray):
    
    """Generate new instance in ai.json"""

    L = [1, 3, 9, 9, 3, 1/24]
    L = [int(len(dataArray) * l) for l in L]
    n = len(L)

    # None Weights
    W = [None for _ in range(n)]
    for index in range(1, n): W[index] = np.random.randn(L[index-1], L[index])

    return UpWei(dataArray, W)


def Spec(dataArray):
    
    """Speculate how an array will evolve with provided ticker and id"""

    # Checker
    if type(dataArray) is not list:
        raise TypeError("StockBot Speculate Module: Input should be a list")

    # Set Input Data for A.I.
    L = [1, 3, 9, 9, 3, 1/24]
    L = [int(len(dataArray) * l) for l in L]

    weightData = json.load(open("ai.json"))
    W = [None for _ in weightData]
    for index in weightData: W[int(index)] = np.array(weightData[index])
    
    X = np.array(dataArray)
    N = np.amax(X, axis=0)
    X = nmath.sigmoid(X / N)

    # A.I.
    AI = NeuralNetwork(L)
    AI.ImportWeight(W)
    specArray = (N * nmath.logit(AI.Forward(X))).tolist()

    return specArray