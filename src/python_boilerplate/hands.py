from python_boilerplate.constants import DICE_COUNT, NUM_SIDES
from python_boilerplate.probability import hand_probability 
from functools import lru_cache
from typing import Dict, Union, Callable
from itertools import product 

def dice_combinations(

        level : int = 0, 
        dice_thrown : int = 5, 
        num_sides : int = 6
        ) -> tuple[tuple[int,...]]:
    
    """
    Generate all possible hands given a input of number of dices thrown and 
    number of sides on a die.
    
    :param level: 
    :type level: int
    :param dice_thrown: number of dices thrown.
    :type dice_thrown: int
    :param n_sides: number of sides of a die
    :type n_sides: int
    :return: 2 dimensioanl numpy array
    :rtype: tuple[tuple[int]]
    """

    possible_throws = []

    def iterate_throws(
            level: int, 
            dice_thrown: int, 
            current : list[int]
            ) -> None:

        if (level == num_sides):
            if (sum(current) == dice_thrown):
                possible_throws.append(tuple(current))

            return 
        
        for i in range(dice_thrown, -1, -1):
            if sum(current) + i <= dice_thrown:
                iterate_throws(level + 1, dice_thrown, current + [i])

    iterate_throws(level, dice_thrown, [])

    return tuple(possible_throws)


def make_table(
        max_throws : int,
        num_sides : int 
        ) -> tuple[tuple[int,...]]:
    
    """
    makes a 2-dimensional numpy array consisting of all hands from one dice
    upp till max_throws. 
    
    :param max_throws: maximum number of throws
    :type max_throws: int
    :param n_sides: number of sides on one die. 
    :type n_sides: int
    :return: returns a 2-dimensional numpy array. 
    :rtype: ndarray[ndarray[int, Any], Any]
    """
    
    all_hands = ()

    for n in range(1, max_throws + 1):
        hands = dice_combinations(dice_thrown=n, num_sides = num_sides)
        all_hands += hands
    
    return all_hands

@lru_cache # Saving the table after calling it the first time
def make_prob_table(
        max_throws : int = DICE_COUNT, 
        num_sides : int = NUM_SIDES
        ) -> Dict[tuple[int], list[Union[float, tuple[int,...]]]]:
    
    table = make_table(max_throws=max_throws, num_sides=num_sides)

    prob_dict = {}

    for hand in table:
        prob = float(hand_probability(hand))

        prob_dict[hand] = [sum(hand), prob]

    return prob_dict

def terminal_state_values(func : Callable[[tuple[int,...]],int]):

    hands = dice_combinations(dice_thrown=DICE_COUNT,num_sides=NUM_SIDES)
    layer = {}

    for h in hands:
        score = func(h)
        layer[h] = score


    return layer

def outcomes(throw : int) ->  Dict[tuple[int,...], list[Union[float, tuple[int,...]]]]:

    prob_table = make_prob_table()

    """
    Given a number of dices to be thrown, the function returns
    a dictionary containing the possible resulting hands and their 
    respective probabilities.
    
    :param throw: number of throws
    :type throw: int
    :return: a dictionary containing tuple as a key, and a list of the number of dices
    and the probability of the given hand. 
    :rtype: Dict[tuple[int], list[float | ndarray[int, Any]]]
    """
    outcome_dict = {key: value for key , value in prob_table.items() if value[0] == throw}
    
    return outcome_dict

def keep_hands(hand : tuple[int,...]) -> tuple[tuple[int,...]]:
    """
    Generates all possible holds for a hand
    
    :param hand: the given hand 
    :type hand: tuple[int]
    :return: return a list of tuples containing different holds.
    :rtype: Any
    """

    results = []
    ranges = [range(x + 1) for x in hand]

    for prod in product(*ranges):
        results.append(prod)

    return results