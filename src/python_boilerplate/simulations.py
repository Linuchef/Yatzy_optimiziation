from python_boilerplate.constants import DIE_FACES, NUM_SIDES, DICE_COUNT, NUM_THROWS
from python_boilerplate.utils import dice_missing, sum_tuples
from random import choice
from typing import Callable, Union
from random import randint
import pandas as pd


def roll_dice(num_roll : int) -> tuple[int,...]:

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
    
    filter_df = df[
    (df["Throws_left"] == throws_left) &  
    (df["Hand"] == hand) & 
    (df["Category_number"] == category)]

    return filter_df["Hold"].values[0]

def generate_hand(hold : tuple[int, ...]) -> tuple[int, ...]:

    num_rerolled = dice_missing(hold)
    dice_rolled = roll_dice(num_rerolled)
    hand = sum_tuples(dice_rolled, hold) 

    return hand
    

def category_score(category : int, df : pd.DataFrame) -> int:

    previous_hand = roll_dice(DICE_COUNT)

    for i in range(1, NUM_THROWS):
        hold = decide_hold(df, previous_hand, NUM_THROWS - i, category)
        next_hand = generate_hand(hold)
        print(previous_hand, hold, next_hand)
        previous_hand = next_hand
    
    score = df[
        (df["Category_number"] == category) & 
        (df["Hand"] == next_hand) &
        (df["Throws_left"] == 0)]["Expected_value"].values[0]
    
    return score

def simulate_forced_yatzy(
        df : pd.DataFrame, 
        num_categories : int = 15
        ) -> int:

    tot_score = 0

    for i in range(num_categories):
        score_category = category_score(i + 1, df)
        tot_score += score_category

        if (i == 5) and (tot_score >= 63):
            tot_score += 50
    
    return tot_score

def simulate_n_times(
        n : int, 
        df : pd.DataFrame
        ) -> list[int]:
    
    score_list = []

    for i in range(n):
        score = simulate_forced_yatzy(df)
        score_list.append(score)

    return score_list




        






    



