from python_boilerplate.constants import NUM_SIDES, DICE_COUNT

def same_face_value(hand : tuple[int,...], face : int) -> int:
    
    return hand[face - 1] * face

def one_pair(hand : tuple[int,...]) -> int:   
    score = 0

    for k,s in enumerate(hand):
        if (s >= 2):
            score = 2 * (k+1)
            

    return score 

def two_pairs(hand : tuple[int,...]) -> int: 

    number_of_pairs = 0
    score = 0

    for i in range(NUM_SIDES - 1, -1, -1):

        if hand[i] >= 2 and number_of_pairs < 2:
            number_of_pairs += 1
            score += (i+1) * 2

        if number_of_pairs == 2:
            break

    if number_of_pairs == 2:
        return score 
    
    else:
        return 0
    
def three_of_a_kind(hand : tuple[int,...]) -> int:
    score = 0

    for i in range(NUM_SIDES - 1, -1, -1):
        if hand[i] >= 3:
            score = (i+1) * 3
            break 

    return score

def four_of_a_kind(hand : tuple[int,...]) -> int:
    score = 0

    for i in range(NUM_SIDES - 1, -1, -1):
        if hand[i] >= 4:
            score = (i+1) * 4
            break 

    return score

def small_straight(hand : tuple[int,...]) -> int:
    score = 0

    for i in range(NUM_SIDES - 1):

        if hand[i] != 1:
            break
            
        if i == NUM_SIDES - 2:
            score = 15

    return score

def large_straight(hand : tuple[int,...]) -> int:
    score = 0

    for i in range(1, NUM_SIDES):

        if hand[i] != 1:
            break
            
        if i == NUM_SIDES - 1:
            score = 20

    return score

def full_house(hand : tuple[int,...]) -> int:

    score = 0
    number_of_matches = 0
    exist_three_of_kind = False
    exist_two_of_a_kind = False
    
    for i in range(NUM_SIDES - 1, -1, -1):

        if (hand[i] >= 2) and number_of_matches < 2:

            if hand[i] >= 3 and not exist_three_of_kind:
                score += (i+1) * 3
                exist_three_of_kind = True
                number_of_matches += 1

            else:
                if not exist_two_of_a_kind:
                    score += (i+1) * 2
                    exist_two_of_a_kind = True
                    number_of_matches += 1
            
    
    if number_of_matches == 2:

        return score 
    
    else:
        return 0


def chance(hand : tuple[int,...]) -> int:
    score = 0
    for k,h in enumerate(hand):
        score += (k+1) * h 

    return score

def yatzy(hand : tuple[int,...]) -> int:

    score = 0

    for i in range(NUM_SIDES):
        if hand[i] == DICE_COUNT:
            score = 50
            
            return score 
    
    return score

    