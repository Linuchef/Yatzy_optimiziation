from python_boilerplate.constants import DIE_FACES, NUM_SIDES
from random import choice
from typing import Callable, Union


def roll_dice(num_roll : int) -> tuple[int,...]:

    if len(DIE_FACES) != NUM_SIDES:
        raise ValueError("NUM_SIDES does not equal the number of elements in DIE_FACES")
    
    for n in num_roll:
        face = choice(DIE_FACES)
        