import datetime as t
import neuralnetwork as nn
import numpy as np
from security import *
from speculate import *
from termcolor import colored

# Set Test Data
testArray = ["TSLA"]
testN = len(testArray)
dateArray = [t.datetime(2021, n + 1, 1) for n in range(12)]

testSecurities = [None for _ in dateArray]
for index, date in enumerate(dateArray):
    testSecurities[index] = [Security(ticker=tick, date=date) for tick in testArray]

openArray = [list(map(lambda x: x.openValues, testSec)) for testSec in testSecurities]
closeArray = [list(map(lambda x: x.openValues, testSec)) for testSec in testSecurities]
highArray = [list(map(lambda x: x.highValues, testSec)) for testSec in testSecurities]
lowArray = [list(map(lambda x: x.lowValues, testSec)) for testSec in testSecurities]

# Next Values
timeIntervals = testSecurities[index][0].length
timeN = timeIntervals//24
dateNextArray = list(map(lambda x: x + t.timedelta(days=timeN), dateArray))

testNextSecurities = [None for _ in dateNextArray]
for index, date in enumerate(dateNextArray):
    testNextSecurities[index] = [Security(ticker=tick, date=date) for tick in testArray]

openNextArray = [list(map(lambda x: x.openValues, testSec)) for testSec in testNextSecurities]
closeNextArray = [list(map(lambda x: x.openValues, testSec)) for testSec in testNextSecurities]
highNextArray = [list(map(lambda x: x.highValues, testSec)) for testSec in testNextSecurities]
lowNextArray = [list(map(lambda x: x.lowValues, testSec)) for testSec in testNextSecurities]

# Set Wights
weightData = json.load(open("ai.json"))
W = [None for _ in weightData]
for index in weightData:
    W[int(index)] = np.array(weightData[index])

# Loop Over Time
L = [1, 3, 9, 9, 3, 1/24]
L = [int(l * (timeIntervals - 1)) for l in L]

fulldW = [np.zeros(shape=weight.shape) for weight in W]

for index in range(timeIntervals):
    for jndex in range(testN-1):
        # Fix Next Values
        openNextArray[index][jndex] = openNextArray[index][jndex][-timeN:]
        closeNextArray[index][jndex] = closeNextArray[index][jndex][-timeN:]
        highNextArray[index][jndex] = highNextArray[index][jndex][-timeN:]
        lowNextArray[index][jndex] = lowNextArray[index][jndex][-timeN:]
        
        # Set Neural Input
        X0 = np.array(openArray[index][jndex])
        N0 = np.amax(X0, axis=0)
        X0 = nmath.sigmoid(X0 / N0)

        X1 = np.array(closeArray[index][jndex])
        N1 = np.amax(X1, axis=0)
        X1 = nmath.sigmoid(X1 / N1)

        X2 = np.array(highArray[index][jndex])
        N2 = np.amax(X2, axis=0)
        X2 = nmath.sigmoid(X2 / N2)

        X3 = np.array(lowArray[index][jndex])
        N3 = np.amax(X3, axis=0)
        X3 = nmath.sigmoid(X3 / N3)
    
        # Set Neural Network
        LoopNeural = nn.NeuralNetwork(L)
        LoopNeural.UpdateWeight(W)
    
        dummy = LoopNeural.Forward(X0)
        R = np.array(openNextArray[index][jndex])
        N = np.amax(R, axis=0)
        R = nmath.sigmoid(R / N)
        dW0 = LoopNeural.Optimisation(R)
    
        dummy = LoopNeural.Forward(X1)
        R = np.array(closeNextArray[index][jndex])
        N = np.amax(R, axis=0)
        R = nmath.sigmoid(R / N)
        dW1 = LoopNeural.Optimisation(R)
        
        dummy = LoopNeural.Forward(X2)
        R = np.array(highNextArray[index][jndex])
        N = np.amax(R, axis=0)
        R = nmath.sigmoid(R / N)
        dW2 = LoopNeural.Optimisation(R)
        
        dummy = LoopNeural.Forward(X3)
        R = np.array(lowNextArray[index][jndex])
        N = np.amax(R, axis=0)
        R = nmath.sigmoid(R / N)
        dW3 = LoopNeural.Optimisation(R)

        for kindex in range(len(dW0)):
            if dW0[kindex] is not None and dW1[kindex] is not None and dW2[kindex] is not None and dW3[kindex] is not None:
                fulldW[kindex] += (dW0[kindex] + dW1[kindex] + dW2[kindex] + dW3[kindex]) / (4 * timeN * testN)
    
# Save New Data
UpWei(openArray, fulldW)
print(colored(f": > A.I. Data Updated", "green"))