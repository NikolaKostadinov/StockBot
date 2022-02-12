import datetime as t, neuralnetwork as nn, numpy as np
from security import *
from speculate import *

testArray = ["TSLA", "AAPL", "ETH", "BTC"]
dateArray = [t.datetime(2021, n+1, 1) for n in range(12)]

testSecurities = [None for _ in dateArray]
for index, date in enumerate(dateArray):
    testSecurities[index] = [Security(ticker=tick, date=date) for tick in testArray]

timeN = testSecurities[index][0].length//24

# R = Secutity(old date).lastValues
# deltaW = AI.Optimisation(R)
# TOTAL deltaW = average(testArray.deltaW) 