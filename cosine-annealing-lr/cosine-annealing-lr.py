import numpy as np 
def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    cosine = np.cos(((np.pi *current_step)/total_steps))
    if cosine == -1 :
        return min_lr
    return min_lr+((base_lr-min_lr)/2) * (1+cosine)
    