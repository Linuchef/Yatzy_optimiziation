from python_boilerplate.solver import build_value_layers
import python_boilerplate.scoring as s 
from python_boilerplate.utils import convert_to_pandas, concatenate_dataframes
import pandas as pd

def optimal_play_table() -> pd.DataFrame:

    # Making the tables for each category

    one_pair = build_value_layers(s.one_pair)
    two_pairs = build_value_layers(s.two_pairs)
    three_of_a_kind = build_value_layers(s.three_of_a_kind)
    four_of_a_kind = build_value_layers(s.four_of_a_kind)
    small_straight = build_value_layers(s.small_straight)
    large_straight = build_value_layers(s.large_straight)
    full_house = build_value_layers(s.full_house)
    chance = build_value_layers(s.chance)
    yatzy = build_value_layers(s.yatzy)

    one_pair_df = convert_to_pandas(one_pair, "one pair")
    two_pairs_df = convert_to_pandas(two_pairs, "two pairs")
    three_of_a_kind_df = convert_to_pandas(three_of_a_kind, "three of a kind")
    four_of_a_kind_df = convert_to_pandas(four_of_a_kind, "four of a kind")
    small_straight_df = convert_to_pandas(small_straight, "small straight")
    large_straight_df = convert_to_pandas(large_straight, "large straight")
    full_house_df = convert_to_pandas(full_house, "full house")
    chance_df = convert_to_pandas(chance, "chance")
    yatzy_df = convert_to_pandas(yatzy, "yatzy")

    df_list = [one_pair_df, two_pairs_df, three_of_a_kind_df, four_of_a_kind_df,
               small_straight_df, large_straight_df, full_house_df, chance_df,
                yatzy_df]
    result_df = concatenate_dataframes(df_list)

    return result_df



