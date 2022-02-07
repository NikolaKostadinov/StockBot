import numpy as np

def sigmoid(input): return 1 / (np.exp(input) + 1)

def sigmoidprime(input): return sigmoid(input) * sigmoid(-input)

def differentiate(function):
    dx = .0001
    return lambda x: (function(x + dx) - function(x)) / dx

def differentiateMore(function, numOfDiff):
    for _ in range(numOfDiff): function = differentiate(function)
    return function

def slopeAt(function, value): return differentiate(function)(value)