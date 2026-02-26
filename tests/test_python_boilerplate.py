import random
from python_boilerplate.hands import last_layer
from python_boilerplate.solver import build_value_layers
from python_boilerplate.utils import convert_to_pandas
import python_boilerplate.scoring as score 

terminal_state = last_layer(score.one_pair)
#print(backward_value_update(layer = terminal_state))
one_pair = build_value_layers(score.one_pair)
print(convert_to_pandas(one_pair))

