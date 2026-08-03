def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    num = 0 
    for i in range(k):
        if recommended[i] in relevant:
            num += 1

    precision = num / k 

    recall = num / len(relevant) 

    return [precision, recall]
        