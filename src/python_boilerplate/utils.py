from python_boilerplate.constants import DICE_COUNT
from typing import Dict
import pandas as pd

def dice_missing(hand : tuple[int,...])-> int:
    n = DICE_COUNT - sum(hand)
    
    if n < 0:
        raise ValueError("Hand contains more dice than allowed")
    
    return n


def convert_to_pandas(
        layers : list[Dict[tuple[int, ...], list[tuple[int, ...], float, int]]],
        category : str
        ) -> pd.DataFrame:
    
    """
    Converting a list of dictionaries to a pandas dataframe.

    :param layers: information about optimal play for each hand
    for each round.
    :type layers: list[Dict[tuple[int, ...], list[tuple[int, ...], float, int]]]
    :param category: category of yatzy (e.g one pair, chance, etc).
    :return: A pandas dataframe consisting of 5 columns.
    :rtype: pd.DataFrame 
    """
    
    rows = []

    for l in layers:
        for hand, (hold, val, throws_left) in l.items():
            rows.append({
                "Hand" : hand,
                "Hold" : hold,
                "Expected value" : val,
                "Throws left" : throws_left,
                "Category" : category
            })

    return pd.DataFrame(rows)

def concatenate_dataframes(list_df : list[pd.DataFrame]) -> pd.DataFrame:
    
    return pd.concat(list_df)
    
