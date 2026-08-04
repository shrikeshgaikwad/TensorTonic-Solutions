import numpy as np

def euclidean_distance(a, b):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    if len(a) != len(b):
        raise ValueError
    sum = 0 
    for i in range(len(a)):
        sum += (a[i] - b[i])**2

    return sum ** 0.5 
        