import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    if num_classes == None:
        num_classes = np.max(y) + 1
    print(num_classes)

    x = []
    # print(y)
    for index in y :
        temp = [0 for i in range(num_classes)]
        temp[index] = 1

        x.append(temp)

    print(x)
    return x
    