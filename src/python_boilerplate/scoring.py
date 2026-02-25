def one_pair(hand : tuple[int,...]) -> int:   
    score = 0

    for k,s in enumerate(hand):
        if (s >= 2):
            score = 2 * (k+1)

    return score 