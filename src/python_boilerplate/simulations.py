from python_boilerplate.constants import DIE_FACES, NUM_SIDES, DICE_COUNT, NUM_THROWS
from python_boilerplate.utils import dice_missing, sum_tuples
from random import choice
import pandas as pd


def roll_dice(num_roll : int) -> tuple[int, ...]:

    """
    roll a specific number of dice, outputs in a frequency tuple. 

    :param num_roll: Number of dice to be rolled.
    :type num_roll: int
    :return: frequency tuple with num_roll rolls. 
    :rtype: tuple[int, ...]
    """

    if len(DIE_FACES) != NUM_SIDES:
        raise ValueError("NUM_SIDES does not equal the number of elements in DIE_FACES")
    
    hand = [0] * NUM_SIDES
    
    for n in range(num_roll):
        face = choice(DIE_FACES)
        hand[face - 1] += 1


    return tuple(hand)

def decide_hold(
        df : pd.DataFrame,
        hand : tuple[int, ...],
        throws_left : int, 
        category : int
        ) -> tuple[int, ...]:
    
    """
    Based on a hand, number of throws left and the category, the 
    function finds the hold yielding the highest expected value.

    :param df: Dataframe of all state values.
    :type df: pd.DataFrame
    :param hand: a given hand of dice
    :type hand: tuple[int, ...]
    :param throws_left: number of throws left of a category
    :type throws_left: int
    :param category: category/round of yatzy (1-15)
    :type category: int
    :return: a hold yielding the largest expected value 
    :rtype: tuple[int, ...]
    """
    
    filter_df = df[
    (df["Throws_left"] == throws_left) &  
    (df["Hand"] == hand) & 
    (df["Category_number"] == category)]

    return filter_df["Hold"].values[0]

def generate_hand(hold : tuple[int, ...]) -> tuple[int, ...]:

    """
    Generates next hand given a hold.

    :param hold: a hold containing less than
    or equal to DICE_COUNT.
    :type hold: tuple[int, ...]
    :return: a tuple with sum DICE_COUNT
    :rtype: tuple[int, ...] 
    """

    num_rerolled = dice_missing(hold)
    dice_rolled = roll_dice(num_rerolled)
    hand = sum_tuples(dice_rolled, hold) 

    return hand
    

def category_score(
        category : int, 
        df : pd.DataFrame, 
        log : bool = False
        ) -> int:

    """
    For a given category/round, find the score after 
    NUM_THROWS throws. 

    :param category: category number (1-15)
    :type category: int
    :param df: dataframe containing all state values.
    :type df: pd.DataFrame
    :param log: a boolean value to decide whether one want to 
    log all the choices in the game
    :return: an integer specifying the score of that 
    category.
    :rtype: int
    """

    previous_hand = roll_dice(DICE_COUNT)

    for i in range(1, NUM_THROWS):

        hold = decide_hold(df, previous_hand, NUM_THROWS - i, category)

        if log:
            print("Current hand : ", previous_hand)
            print("Optimal hold : ", hold)

        next_hand = generate_hand(hold)
        previous_hand = next_hand
    
    score = df[
        (df["Category_number"] == category) & 
        (df["Hand"] == next_hand) &
        (df["Throws_left"] == 0)]["Expected_value"].values[0]

    if log:
        print("last hand : ", next_hand)
        print()
        print("Score of round : ", score)
        print()
    
    return score

def simulate_forced_yatzy(    
        df : pd.DataFrame, 
        num_categories : int = 15,
        log : bool = False
        ) -> int:
    
    """
    Simulates a game of forced yatzy playing optimally.

    :param df: dataframe containing all state values.
    :type df: pd.DataFrame
    :param num_categories: number of categories looked at
    (default is set to 15)
    :type num_categories: int = 15
    :param log: if set to true, prints out all choices and happenings
    :type log: bool
    :return: the total score of simulated game.
    :rtype: int
    """

    tot_score = 0

    for i in range(num_categories):

        if log:
            category_name = df[(df["Category_number"] == i + 1)]["Category_name"].values[0] 
            print()
            print(f"--------------- {category_name}-----------------")
            print()
            print("Current score : ", tot_score)

        score_category = category_score(i + 1, df, log = log)
        tot_score += score_category

        if log:
            print("Current score : ", tot_score)


    

        if (i == 5) and (tot_score >= 42):
            tot_score += 50

            print()
            print("Score in first half is over 42")
            print("Current score : ", tot_score)
            print()
    
    return tot_score

def simulate_n_times(
        n : int, 
        df : pd.DataFrame
        ) -> list[int]:
    
    """
    Simulates n games of forced yatzy playing 
    optimally.

    :param n: number of simulated games
    :type n: int
    :param df: dataframe containing all state values
    :type df: pd.DataFrame
    :param log: if set to true, prints out all choices and happenings
    :type log: bool
    :return: a list with n scores from all 
    n simulated yatzy games
    :rtype: list[int]
    """
    
    score_list = []

    for i in range(n):
        score = simulate_forced_yatzy(df)
        score_list.append(score)


    return score_list




        






    



