from python_boilerplate.hands import outcomes, dice_combinations, keep_hands
from python_boilerplate.utils import dice_missing
from python_boilerplate.constants import DICE_COUNT, NUM_SIDES
from typing import Dict

def expected_value_for_hold(
        state_values : Dict[tuple[int,...], float], 
        held_dice: tuple[int,...],
        num_rerolled : int
        ) -> float: 
    
    """
    Find expected score for a specific hold of dices.  
    
    :param state_values: Current dictionary of maximum expected 
    scores after a specific number of throws for a given hand.
    :type state_values: Dict[tuple[int], float]
    :param held_dice: a vector of current hold of dice
    :type held_dice: tuple[int,...]
    :param num_rerolled: number of dices to be thrown
    :type num_rerolled: int
    :return: returns the expected score.
    :rtype: float
    """

    current_val = 0
    outcomes_throw = outcomes(throw = num_rerolled) # Find probability for all combinations of throws

    for key in outcomes_throw.keys():
        resulting_hand = tuple(a + b for a,b in zip(held_dice, key)) # Element wise addition 
        current_val += outcomes_throw[key][1] * state_values[resulting_hand]
    
    return current_val

def maximize_expected_value (
        state_values : Dict[tuple[int,...], float],
        holds : tuple[tuple[int,...]]
        ) -> list[tuple[int,...], int]:
    
    """
    Finds the held dice of a hand yielding the biggest expected value. 
    
    :param state_values: Current dictionary of maximum expected 
    scores after a specific number of throws for a given hand.
    :type state_values: Dict[tuple[int, ...], float]
    :param holds: a tuple containing all possible holds for a hand
    :type holds: tuple[tuple[int, ...]]
    :return: the held dice with best expectation along with its expectation. 
    :rtype: list[tuple[int, ...], int]
    """
    
    val = 0
    best_hold = ()

    for h in holds:
        num_rerolled = dice_missing(h)
        expected_val = expected_value_for_hold(
            state_values=state_values, 
            held_dice = h, 
            num_rerolled = num_rerolled)
        
        if expected_val > val:
            val = expected_val
            best_hold = h
    
    return [best_hold, val]

def find_previous_state_values(
        state_values : Dict[tuple[int,...],float]
        )-> Dict[tuple[int,...],float]:
    
    """
    Function that returns a dictionary containing all optimal 
    expected values belonging to all hands from the previous state. 
    
    :param state_values: current state values
    :type state_values: Dict[tuple[int, ...], float]
    :return: Previous state values
    :rtype: Dict[tuple[int, ...], float]
    """

    previous_state_values = {}
    
    hand_combinations = dice_combinations(
        dice_thrown = DICE_COUNT, 
        num_sides = NUM_SIDES)
    
    for hand in hand_combinations:

        holds = keep_hands(hand = hand)
        optimal_hold = maximize_expected_value(state_values = state_values, holds = holds)

        previous_state_values[hand] = optimal_hold[1]

    return previous_state_values

    