import numpy as np, nmath
from numpy import shape

class NeuralNetwork:
    def __init__(self, W):
        
        """Set a neural network"""
        
        if type(W) is list: self.W = W
        else: TypeError("StockBot Neural Module: Weight input should be a list")
        
        for _, this in enumerate(self.W):
            if type(this) is not np.ndarray: TypeError(f"StockBot Neural Module: {this} should be a numpy matrix")
        
        self.layersLength = len(self.W)
        
        # Activation and "Semiactivation" Matrices
        self.A = [None for _ in range(self.layersLength)]
        self.Z = [None for _ in range(self.layersLength)]
        
    def Forward(self, X):
        
        """Forward Propagate (return output data)"""
        
        # Forward Math:
        # A{0} = X
        # Z{n} = W{n} A{n-1}
        # A{n} = σ( Z{n} )
        
        # Cheker
        if X.shape != self.W[0].shape: TypeError("StockBot Neural Module: Input matrix and weight matrix should have the same dimensionality")
        
        # Normalize
        X = X / np.max(X, axis=0)
        
        # Compute Matrices
        self.A[0] = X

        for index in range(1, self.layersLength):
            self.Z[index] = np.dot(self.W[index], self.A[index-1])
            self.A[index] = nmath.sigmoid(self.Z[index])

        # Return
        return self.A[-1]
    
    def Error(self, R):
        
        """Return error values of the neural network"""
        
        # Error Math:
        # err = A{-1} - R
        
        # Normalize
        R = R / np.max(R, axis=0)
        
        # Compute Errors
        return self.A[-1] - R
    
    def TotalError(self, R):
        
        """Return total error of the neural network"""
        
        # Total Error Math:
        # err = Σ<over rows> ( A{-1}<row> - R<row> )²
        
        return sum(self.Error(R)**2)
        
    
    def Backward(self, R):
        
        """Backpropagation (train neural network)"""
        
        # Backward Math:
        # δ{-1} = (A{-1} - R) o σ'( Z{-1} )
        # δ{n} = W*{n+1} δ{n+1} o σ'( Z{n} )
        # ΔW{n} = - δ{n} A*{n-1}
        
        # Normalize
        R = R / np.max(R, axis=0)
        
        # Delta Matrices
        delta = [None for _ in range(self.layersLength)]
        delta[-1] = np.multiply(self.A[-1] - R, nmath.sigmoidprime(self.Z[-1]))
        
        for index in range(self.layersLength-1, 0, -1):
            delta[index] = np.dot(delta[index+1], self.W[index].T)
        
        # Update Weights
        for index in range(1, self.layersLength):
            self.W[index] = self.W[index] - np.dot(self.A[index-1].T, delta[index])