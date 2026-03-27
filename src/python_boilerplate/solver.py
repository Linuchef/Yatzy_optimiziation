from python_boilerplate.hands import outcomes, dice_combinations, keep_hands, last_layer
from python_boilerplate.utils import dice_missing
from python_boilerplate.constants import DICE_COUNT, NUM_SIDES, NUM_THROWS
from typing import Dict, Callable, Union

def expected_value_for_hold (
        layer : tuple[
            Dict[tuple[int,...], list[None, int, int]], 
            Dict[tuple[int,...], Dict[int, float]]
            ], 
        held_dice: tuple[int,...],
        num_rerolled : int
        ) -> tuple[
            float,
            Dict[int, float]
        ]: 
    
    """
    Find expected score and probability distribution for a specific hold of dices.  
    
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
    layer_expected_value = layer[0]
    layer_prob_dist = layer[1]
    prob_dict = {}

    for key in outcomes_throw.keys():
        resulting_hand = tuple(a + b for a,b in zip(held_dice, key)) # Element wise addition 
        current_val += outcomes_throw[key][1] * layer_expected_value[resulting_hand][1]

        ###### Managing the probability distribution of the hold ######
        hand_score_distribution = layer_prob_dist[resulting_hand]

        for score, prob in hand_score_distribution.items():

            if score in prob_dict:

                prob_dict[score] += prob * outcomes_throw[key][1]
            
            else:
                prob_dict[score] = prob * outcomes_throw[key][1]

    
    return (current_val, prob_dict)

def maximize_expected_value (
        layer : tuple[
            Dict[tuple[int,...], list[None, int, int]], 
            Dict[tuple[int,...], Dict[int, float]]
            ],
        holds : tuple[tuple[int,...]]
        ) -> tuple[
                list[
                    tuple[int,...], 
                    int
                    ],
                    Dict[int, float]]:
    
    """
    Finds the held dice of a hand yielding the biggest expected value. 
    
    :param layer: Current dictionary of maximum expected 
    scores after a specific number of throws for a given hand.
    :type layer: Dict[tuple[int, ...], float]
    :param holds: a tuple containing all possible holds for a hand
    :type holds: tuple[tuple[int, ...]]
    :return: the held dice with best expectation along with its expectation. 
    :rtype: tuple[
                list[
                    tuple[int,...], 
                    int
                    ],
                    Dict[int, float]]:
    """
    
    val = 0
    best_hold = ()

    for h in holds:
        num_rerolled = dice_missing(h)
        expected_val = expected_value_for_hold(
            layer=layer, 
            held_dice = h, 
            num_rerolled = num_rerolled)
        
        if expected_val[0] > val:
            val = expected_val[0]
            best_hold = h
            prob_dist = expected_val[1]
    
    return ([best_hold, val], prob_dist)

def backward_value_update (
        layer : Dict[tuple[int,...],int],
        throws_left : int
        )-> tuple[
                Dict[
                    tuple[int,...], 
                    list[
                        tuple[int,...],
                        int,
                        int
                        ]
                ],
                Dict[int, float]
        ]:
    
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
    previous_prob_distr_layer = {}
    
    hand_combinations = dice_combinations(
        dice_thrown = DICE_COUNT, 
        num_sides = NUM_SIDES)
    
    for hand in hand_combinations:

        holds = keep_hands(hand = hand)
        maximized_value = maximize_expected_value(layer = layer, holds = holds)
        optimal_hold = maximized_value[0]
        optimal_hold.append(throws_left)

        previous_layer_with_hold[hand] = optimal_hold
        previous_prob_distr_layer[hand] = maximized_value[1]

    return (previous_layer_with_hold, previous_prob_distr_layer)

def build_value_layers(
        score_func : Union[
            Callable[
                [tuple[int,...]],int], 
            Callable[
                [tuple[int,...], int], int]],

        face : int = None
        ) -> tuple[
            list[
                Dict[
                    tuple[int,...],float]],
            list[
                Dict[
                    tuple[int, ...], Dict[int, float]
                    ]]]:
    
    """
    Calculate all the layers and put them in a list.
    
    :param score_func: yatzee round
    :type score_func: Callable[[tuple[int, ...]], int]
    :param face: input of score function. Default is set to None
    :type face: int
    :return: Returns a list of dictionaries containing optimal
    expected values for a given hand after a certain throw. 
    :rtype: list[Dict[tuple[int, ...], float]]
    """
    
    value_layers = []
    prob_layers = []

    layer = last_layer(score_func, face)
    value_layers.append(layer[0])
    prob_layers.append(layer[1])

    for i in range(NUM_THROWS - 1):

        previous_layer = backward_value_update(layer = layer, throws_left = i + 1)
        layer = previous_layer
        value_layers.append(layer[0])
        prob_layers.append(layer[1])

    return (value_layers, prob_layers)



    



    