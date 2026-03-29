from python_boilerplate.probability import hand_probability
from python_boilerplate.solver import build_value_layers
from python_boilerplate.scoring import same_face_value
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

def find_category_distribution (
        score_func : Union[
            Callable[
                [tuple[int,...]],int], 
            Callable[
                [tuple[int,...], int], int]],
        face : int = None
) -> dict[int, float]:
    
    prob_dict = {}
    
    if face == None:
        
        prob_distribution = build_value_layers(score_func)[1][-1]
    
    else:

        prob_distribution = build_value_layers(score_func, face)[1][-1]
    
    for hand, pair in prob_distribution.items():

        for score, prob in pair.items():

            if score in prob_dict:

                prob_dict[score] += hand_probability(hand) * prob
            
            else:
                prob_dict[score] = hand_probability(hand) * prob
    return prob_dict

def extra_points_prob(extra_points_thresh : int = 42) -> float:

    prob_list = []
    for i in range(1,7):
        prob_dict = find_category_distribution(same_face_value, i)
        prob_list.append(prob_dict)

    def iterate_recursive (
            index : int, 
            current_sum : float,
            current_prob : float) -> float:

        if index == 6:
            if current_sum >= extra_points_thresh:
                return current_prob
            else:
                return 0
            
        total_prob = 0
        current_distribution = prob_list[index]

        for score, prob in current_distribution.items():

            total_prob += iterate_recursive(
                index + 1, 
                current_sum + score, 
                current_prob * prob)

        return total_prob

    return iterate_recursive(0, 0, 1)


def expected_value_for_game(
        df : pd.DataFrame, 
        bonus_point : int = 50) -> float:

    bonus_prob = extra_points_prob()

    return df['Optimal_score'].sum() + bonus_point * bonus_prob




    
        



