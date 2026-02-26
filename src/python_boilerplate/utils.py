from python_boilerplate.constants import DICE_COUNT
from typing import Dict
import pandas as pd

def dice_missing(hand : tuple[int,...])-> int:
    n = DICE_COUNT - sum(hand)
    
    if n < 0:
        raise ValueError("Hand contains more dice than allowed")
    
    return n


def convert_to_pandas(
        layers : list[Dict[tuple[int, ...], list[tuple[int, ...], float, int]]]
        ) -> pd.DataFrame:
    
    rows = []

    for l in layers:
        for hand, (hold, val, throws_left) in l.items():
            rows.append({
                "Hand" : hand,
                "Hold" : hold,
                "Expected value" : val,
                "Throws left" : throws_left
            })

    return pd.DataFrame(rows)
    
