def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    cnt = 0 
    for i in range(len(recommendations)):
        for j in range(k):
            if ground_truth[i][0] == recommendations[i][j]:
                cnt += 1 


    hit_rate = cnt / len(recommendations)
    return hit_rate