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

    
