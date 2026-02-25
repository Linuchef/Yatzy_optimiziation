from math import factorial

def hand_probability(hand : tuple[int,...]) -> float:
    """
    Docstring for hand_probability
    
    :param hand: Description
    :type hand: np.ndarray[int]
    :return: Description
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