import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.01, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    shape = X.shape
    x_dim = shape[0]
    y_dim = shape[1]
    # print(x_dim, y_dim)
    # print(y.shape)
    
    w = np.zeros((y_dim,1),dtype=float)
    b = np.random.rand(1)
    # print(w, b)
    
    for step in range(steps):
        z = np.dot(X,w) + b 
        a = _sigmoid(z)
        a = np.where(a >= 0.5 , 1 , 0)
        a = a.flatten()
        
        e = y - a 
        e = np.reshape(e,(1,x_dim))
        
        w = w + lr* (np.dot(X.T,e.T))
        b = b + lr*e.mean()
        
    w = w.flatten()    
    b = b.flatten()
    
    return (w, b)