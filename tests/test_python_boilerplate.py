import random
from python_boilerplate.hands import last_layer, keep_hands, outcomes, make_prob_table
from python_boilerplate.solver import build_value_layers, expected_value_for_hold, maximize_expected_value, backward_value_update
from python_boilerplate.utils import convert_to_pandas
from python_boilerplate.simulations import generate_hand
from python_boilerplate.expected_score import find_category_distribution, extra_points_prob, expected_value_for_game
from python_boilerplate.make_df import category_score
import python_boilerplate.scoring as score 

last_layer_dict = last_layer(score.chance)
#hold_prob = expected_value_for_hold(last_layer_dict,(0, 0, 0, 0, 1, 2), 2)[1]
#print(maximize_expected_value(last_layer_dict, ((0,3,0,0,0,0), (0,0,1,2,0,0), (0,0,0,0,0,3)))[1])
#backward_layer = backward_value_update(last_layer_dict, 1)
#print(find_category_distribution(score.full_house))
df = category_score()
print(expected_value_for_game(df))
