from python_boilerplate.constants import DICE_COUNT

def dice_missing(hand : tuple[int,...])-> int:
    n = DICE_COUNT - sum(hand)
    
    if n < 0:
        raise ValueError("Hand contains more dice than allowed")
    
    return n
    
