import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.array(x)
    # Write code here
    return np.maximum(x, x*alpha)