import numpy as np
import nmath


class NeuralNetwork:
    def __init__(self, H):
        
        """Set a neural network"""

        self.layersLength = len(H)

        # Random Weights
        self.W = [None for _ in range(self.layersLength)]

        for index in range(1, self.layersLength):
            self.W[index] = np.random.randn(H[index-1], H[index])

        # Activation and "Semiactivation" Matrices
        self.A = [None for _ in range(self.layersLength)]
        self.Z = [None for _ in range(self.layersLength)]

    def ImportWeight(self, W):
        
        """Import weight data to neural network"""

        if type(W) is list: self.W = W
        else:TypeError("StockBot Neural Module: Weight input should be a list")

        for _, this in enumerate(self.W):
            if type(this) is not np.ndarray:
                TypeError(f"StockBot Neural Module: {this} should be a numpy matrix")

        self.W = W

    def Forward(self, X):
        
        """Propagate forward (return output data)"""
        
        X = np.append(X, 0)
        self.A[0] = X
        
        # Compute Matrices
        for index in range(1, self.layersLength):
            self.Z[index] = np.dot(self.A[index-1], self.W[index])
            self.A[index] = nmath.sigmoid(self.Z[index])

        # Return
        return self.A[-1]

    def Forwards(self, Xs):
        
        """Return an array of forward propagation"""

        return [self.Forward(X) for X in Xs]

    def Error(self, R):
        
        """Return error values of the neural network"""

        return self.A[-1] - R

    def TotalError(self, R):
        
        """Return total error of the neural network"""

        return sum(self.Error(R)**2)

    def Optimisation(self, R):
        
        """Return optimisation for network weights"""

        learrate = np.log(np.pi)

        # Initiate Matrices
        delta = [None for _ in range(self.layersLength)]
        delta[-1] = np.multiply(self.A[-1] - R, nmath.sigmoidprime(self.Z[-1]))

        deltaW = [None for _ in range(self.layersLength)]
        deltaW[-1] = -np.dot(self.A[-1].T, delta[-1])

        # Delta Matrices
        for index in range(self.layersLength-2, 0, -1):
            delta[index] = np.dot(
                delta[index+1], self.W[index+1].T) * nmath.sigmoidprime(self.Z[index])

        # Optimisation
        deltaW = [None for _ in range(self.layersLength)]
        for index in range(1, self.layersLength-1):
            deltaW[index] = - learrate * np.dot(self.A[index].T, delta[index])

        return deltaW

    def UpdateWeight(self, deltaW):
        
        """Update weights"""

        for index in range(1, self.layersLength):
            if deltaW[index] is not None:
                self.W[index] = self.W[index] + deltaW[index]

    def Backward(self, R):
        
        """Backpropagation (train neural network)"""

        self.UpdateWeight(self.Optimisation(R))
