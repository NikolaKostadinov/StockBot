import numpy as np, nmath

class NeuralNetwork:
    def __init__(self, _weights):
        
        """Set a neural network"""
        
        if type(_weights) is list: self.W = _weights
        else: TypeError("StockBot Neural Module: Weight input should be a list")
        
        for _, this in enumerate(self.W):
            if type(this) is not np.ndarray: TypeError(f"StockBot Neural Module: {this} should be a numpy matrix")
        
        self.leyersLength = len(self.W)
        
    def Forward(self, X):
        
        """Forward Propagate (return output data)"""
        
        # Forward Math:
        # X{0} = X
        # Z{n} = W{n} X{n-1}
        # X{n} = σ( Z{n} )
    
    def Error(self, R):
        
        """Return error values of the neural network"""
        
        # Error Math:
        # err = ( X{-1} - R )²
    
    def TotalError(self, R):
        
        """Return total error of the neural network"""
        
        # Total Error Math:
        # err = Σ<over rows> ( X{-1}<row> - R<row> )²
    
    def Backward(self, R):
        
        """Backpropagation (train neural network)"""
        
        # Backward Math:
        # δ{-1} = (X{-1} - R) o σ'( Z{-1} )
        # δ{n} = W*{n+1} δ{n+1} o σ'( Z{n} )
        # ΔW{-1} = - δ{n} X*{n-1}     