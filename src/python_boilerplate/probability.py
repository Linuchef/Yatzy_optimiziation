from math import factorial

def hand_probability(hand : tuple[int,...]) -> float:
    """
    Finds the probability of getting the specific hand.
    
    :param hand: A tuple consisting of the frequency of
    eyes on the dice. 
    :type hand: np.ndarray[int]
    :return: Returns a float describing the probability
    of the hand. 
    :rtype: float
    """

    n_faculty = factorial(sum(hand))
    n_sides = len(hand)
    c = 1
    prod = n_faculty
    ordered_throws = n_sides**(sum(hand))

    while c <= n_sides:
        prod *= 1/factorial(hand[c-1])

        c += 1

    return prod / ordered_throws