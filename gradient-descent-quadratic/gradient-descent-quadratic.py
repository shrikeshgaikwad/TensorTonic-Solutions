def gradient_descent_quadratic(a, b, c, x, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps*2):
        x = x  - (lr * (2 *a*x + b)) 
    return x