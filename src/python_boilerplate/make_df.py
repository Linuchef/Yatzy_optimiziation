from python_boilerplate.solver import build_value_layers
import python_boilerplate.scoring as s 
from python_boilerplate.utils import convert_to_pandas
import pandas as pd

def optimal_play_table() -> pd.DataFrame:

    # Making the tables for each category
    ones = build_value_layers(s.same_face_value, 1)
    twos = build_value_layers(s.same_face_value, 2)
    threes = build_value_layers(s.same_face_value, 3)
    fours = build_value_layers(s.same_face_value, 4)
    fives = build_value_layers(s.same_face_value, 5)
    sixes = build_value_layers(s.same_face_value, 6)
    one_pair = build_value_layers(s.one_pair)
    two_pairs = build_value_layers(s.two_pairs)
    three_of_a_kind = build_value_layers(s.three_of_a_kind)
    four_of_a_kind = build_value_layers(s.four_of_a_kind)
    small_straight = build_value_layers(s.small_straight)
    large_straight = build_value_layers(s.large_straight)
    full_house = build_value_layers(s.full_house)
    chance = build_value_layers(s.chance)
    yatzy = build_value_layers(s.yatzy)

    ones_df = convert_to_pandas(ones, "ones", 1)
    twos_df = convert_to_pandas(twos, "twos", 2)
    threes_df = convert_to_pandas(threes, "threes", 3)
    fours_df = convert_to_pandas(fours, "fours", 4)
    fives_df = convert_to_pandas(fives, "fives", 5)
    sixes_df = convert_to_pandas(sixes, "sixes", 6)
    one_pair_df = convert_to_pandas(one_pair, "one pair", 7)
    two_pairs_df = convert_to_pandas(two_pairs, "two pairs", 8)
    three_of_a_kind_df = convert_to_pandas(three_of_a_kind, "three of a kind", 9)
    four_of_a_kind_df = convert_to_pandas(four_of_a_kind, "four of a kind", 10)
    small_straight_df = convert_to_pandas(small_straight, "small straight", 11)
    large_straight_df = convert_to_pandas(large_straight, "large straight", 12)
    full_house_df = convert_to_pandas(full_house, "full house", 13)
    chance_df = convert_to_pandas(chance, "chance", 14)
    yatzy_df = convert_to_pandas(yatzy, "yatzy", 15)

    df_list = [ones_df, twos_df, threes_df, fours_df, 
               fives_df, sixes_df, one_pair_df, two_pairs_df, 
               three_of_a_kind_df, four_of_a_kind_df, small_straight_df, large_straight_df, 
               full_house_df, chance_df, yatzy_df]
    
    result_df = pd.concat(df_list)

    return result_df



