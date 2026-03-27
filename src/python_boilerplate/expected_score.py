from python_boilerplate.probability import hand_probability
from typing import Callable, Union
import pandas as pd

def find_category_score(
        df : pd.DataFrame, 
        cat_num : int) -> dict[str, float]:

    filtered_df = df[df["Category_number"] == cat_num]

    sum_score = 0  # The current expected score of the category

    for i in filtered_df.index:

        prob_hand = hand_probability(filtered_df.loc[i, "Hand"])
        sum_score += prob_hand * float(filtered_df.loc[i, "Expected_value"])

    return {
        "Category_name" : filtered_df["Category_name"].iloc[0],
        "Optimal_score" : sum_score
        }

