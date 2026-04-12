import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    print(x)
    x = np.asarray(x, dtype = float)
    print(x)
    
    result = []
    
    
    y = 1/(1+(np.exp(-x)))
    print("hi")
    return y