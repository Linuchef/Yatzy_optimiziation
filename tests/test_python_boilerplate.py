import random
from python_boilerplate.hands import last_layer
from python_boilerplate.solver import maximize_expected_value, backward_value_update, build_value_layers
import python_boilerplate.scoring as score 

terminal_state = last_layer(score.one_pair)
#print(backward_value_update(layer = terminal_state))
print(build_value_layers(score.one_pair))



