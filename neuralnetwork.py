import numpy as np, nmath

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
        
        """"""
        
        if type(W) is list: self.W = W
        else: TypeError("StockBot Neural Module: Weight input should be a list")
        
        for _, this in enumerate(self.W):
            if type(this) is not np.ndarray: TypeError(f"StockBot Neural Module: {this} should be a numpy matrix")
            
        self.W = W
    
    def Forward(self, X):
        
        """Forward Propagate (return output data)"""
        
        # Forward Math:
        # A{0} = X
        # Z{n} = W{n} A{n-1}
        # A{n} = σ( Z{n} )
        
        # Compute Matrices
        self.A[0] = X

        for index in range(1, self.layersLength):
            self.Z[index] = np.dot(self.A[index-1], self.W[index])
            self.A[index] = nmath.sigmoid(self.Z[index])

        # Return
        return self.A[-1]
    
    def Error(self, R):
        
        """Return error values of the neural network"""
        
        # Error Math:
        # err = A{-1} - R
        
        # Compute Errors
        return self.A[-1] - R
    
    def TotalError(self, R):
        
        """Return total error of the neural network"""
        
        # Total Error Math:
        # err = Σ<over rows> ( A{-1}<row> - R<row> )²
        
        return sum(self.Error(R)**2)
        
    def Optimisation(self, R):
        
        """"""
        
        # Backward Math:
        # δ{-1} = (A{-1} - R) o σ'( Z{-1} )
        # δ{n} = W*{n+1} δ{n+1} o σ'( Z{n} )
        # ΔW{n} = - δ{n} A*{n-1}
        
        learrate = np.e
        
        # Initiate Matrices
        delta = [None for _ in range(self.layersLength)]
        delta[-1] = np.multiply(self.A[-1] - R, nmath.sigmoidprime(self.Z[-1]))
        
        deltaW = [None for _ in range(self.layersLength)]
        deltaW[-1] = -np.dot(self.A[-1].T, delta[-1])
        
        # Delta Matrices
        for index in range(self.layersLength-2, 0, -1):
            delta[index] = np.dot(delta[index+1], self.W[index+1].T) * nmath.sigmoidprime(self.Z[index])
            
        # Optimisation
        deltaW = [None for _ in range(self.layersLength)]
        for index in range(1, self.layersLength-1):
            deltaW[index] = - learrate * np.dot(self.A[index].T, delta[index])
            
        return deltaW
    
    def Backward(self, R):
        
        """Backpropagation (train neural network)"""
        
        deltaW = self.Optimisation(R)
        
        # Update Weights
        for index in range(1, self.layersLength):
            if deltaW[index] is not None:
                self.W[index] = self.W[index] + deltaW[index]