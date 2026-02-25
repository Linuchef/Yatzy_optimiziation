import random
from python_boilerplate.hands import terminal_state_values, keep_hands
from python_boilerplate.solver import maximize_expected_value, find_previous_state_values
import python_boilerplate.scoring as score 

terminal_state = terminal_state_values(score.one_pair)
print(find_previous_state_values(state_values = terminal_state))




