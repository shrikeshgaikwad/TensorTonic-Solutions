import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.array(x)
    result = []

    for i in q :
        result.append(np.percentile(x, i))

    return np.array(result)