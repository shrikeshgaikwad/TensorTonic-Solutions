import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if np.sum(p) != 1 :
        raise ValueError 
        
        

    sum = 0 

    for i in range(len(x)):
        sum += x[i]*p[i]


    return sum 

      

        

    
