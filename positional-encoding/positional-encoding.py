import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    freq = []
    a = []
    n = np.where(d_model%2 == 0, d_model/2 , d_model//2 + 1)
    print(n)
    for i in range(int(n)) :
        f = 1/(base**(2*i/d_model))
        freq.append(f)
        
    for i in range(seq_len):
        for f in range(len(freq)):
            a.append(np.sin(i*freq[f]))
            if (d_model % 2 != 0) and (f == len(freq) - 1 ):
                continue
            a.append(np.cos(i*freq[f]))

    a = np.array(a)
    a = a.reshape(seq_len,d_model)
            
    return a 
    