from python_boilerplate.hands import outcomes, dice_combinations, keep_hands, last_layer
from python_boilerplate.utils import dice_missing
from python_boilerplate.constants import DICE_COUNT, NUM_SIDES, NUM_THROWS
from typing import Dict, Callable

def expected_value_for_hold(
        layer : Dict[tuple[int,...], float], 
        held_dice: tuple[int,...],
        num_rerolled : int
        ) -> float: 
    
    """
    Find expected score for a specific hold of dices.  
    
    :param layer: Current dictionary of maximum expected 
    scores after a specific number of throws for a given hand.
    :type layer: Dict[tuple[int], float]
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
        current_val += outcomes_throw[key][1] * layer[resulting_hand][1]
    
    return current_val

def maximize_expected_value (
        layer : Dict[tuple[int,...], float],
        holds : tuple[tuple[int,...]]
        ) -> list[tuple[int,...], int]:
    
    """
    Finds the held dice of a hand yielding the biggest expected value. 
    
    :param layer: Current dictionary of maximum expected 
    scores after a specific number of throws for a given hand.
    :type layer: Dict[tuple[int, ...], float]
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
            layer=layer, 
            held_dice = h, 
            num_rerolled = num_rerolled)
        
        if expected_val > val:
            val = expected_val
            best_hold = h
    
    return [best_hold, val]

def backward_value_update (
        layer : Dict[tuple[int,...],int],
        throws_left : int
        )-> any:
    
    """
    Function that returns a dictionary containing all optimal 
    expected values belonging to all hands from the previous layer. 
    
    :param layer: current state values
    :type layer: Dict[tuple[int, ...], float]
    :param throws_left: Number of throws left for a given round
    :type throws_left: int
    :return: Previous state values
    :rtype: Dict[tuple[int, ...], float]
    """

    previous_layer_with_hold = {}
    
    hand_combinations = dice_combinations(
        dice_thrown = DICE_COUNT, 
        num_sides = NUM_SIDES)
    
    for hand in hand_combinations:

        holds = keep_hands(hand = hand)
        optimal_hold = maximize_expected_value(layer = layer, holds = holds)
        optimal_hold.append(throws_left)

        previous_layer_with_hold[hand] = optimal_hold

    return previous_layer_with_hold

def build_value_layers(
        score_func : Callable[[tuple[int,...]],int]
        ) -> list[Dict[tuple[int,...],float]]:
    
    """
    Calculate all the layers and put them in a list.
    
    :param score_func: yatzee round
    :type score_func: Callable[[tuple[int, ...]], int]
    :return: Returns a list of dictionaries containing optimal
    expected values for a given hand after a certain throw. 
    :rtype: list[Dict[tuple[int, ...], float]]
    """
    
    value_layers = []

    layer = last_layer(score_func)
    value_layers.append(layer)

    for i in range(NUM_THROWS - 1):

        previous_layer = backward_value_update(layer = layer, throws_left = i + 1)
        layer = previous_layer
        value_layers.append(layer)

    return value_layers




    