from python_boilerplate.constants import DICE_COUNT
from typing import Dict
import pandas as pd

def dice_missing(hand : tuple[int,...])-> int:
    n = DICE_COUNT - sum(hand)
    
    if n < 0:
        raise ValueError("Hand contains more dice than allowed")
    
    return n

def sum_tuples(x : tuple[int,...], y : tuple[int, ...]) -> tuple[int, ...]:

    return tuple(a + b for a,b in zip(x,y))

def frequency_to_value(x : tuple[int,...]) -> tuple[int,...]:
    hand = []

    if x == None:
        return None
    
    for val,freq in enumerate(x):

        if freq > 0:

            for i in range(freq):
                hand.append(val + 1)

    return tuple(hand)

def format_tuple(x : tuple[int, ...]) -> str:

    if x == ():
        return "-"
    
    if x == None:
        return "N/A"
    
    return "(" + ", ".join(map(str, x)) + ")"



def convert_to_pandas(
        layers : list[Dict[tuple[int, ...], list[tuple[int, ...], float, int]]],
        category_name : str,
        category_num : int
        ) -> pd.DataFrame:
    
    """
    Converting a list of dictionaries to a pandas dataframe.

    :param layers: information about optimal play for each hand
    for each round.
    :type layers: list[Dict[tuple[int, ...], list[tuple[int, ...], float, int]]]
    :param category_name: name of category (e.g one pair, chance, etc).
    :type category_name: str
    :param category_num: number of the sequences of the categories (e.g ones = first category, 
    twos = second category, ..., yatzy = fifteenth category).
    :type category_num: int
    :return: A pandas dataframe consisting of 5 columns.
    :rtype: pd.DataFrame 
    """
    
    rows = []

    for l in layers:
        for hand, (hold, val, throws_left) in l.items():
            rows.append({
                "Hand" : hand,
                "Hold" : hold,
                "Expected_value" : val,
                "Throws_left" : throws_left,
                "Category_name" : category_name,
                "Category_number" : category_num
            })

    return pd.DataFrame(rows)

def change_dice_representation(df : pd.DataFrame) -> pd.DataFrame:
    
    df["Hand"] = df["Hand"].apply(frequency_to_value)
    df["Hold"] = df["Hold"].apply(frequency_to_value)

    df["Hand"] = df["Hand"].apply(format_tuple)
    df["Hold"] = df["Hold"].apply(format_tuple)

    df = df.rename(columns={
        "Expected_value" : "Expected Value",
        "Throws_left" : "Throws left",
        "Category_name" : "Category name"
    })

    df = df.drop(columns=["Category_number"])

    return df


    