import math, random
from typing import Union

def time_to_minutes(time: int) -> str:
    minutes = str(time//60)
    seconds = time % 60
    seconds = f"{seconds:02d}"
    return minutes+":"+seconds

def random_pos(tolerance: int, maxwidth: int, maxheight: int, char_pos:tuple((int, int))=(-1000, -1000), targ_pos:tuple((int, int))=(-1000, -1000)) -> tuple((int, int)):
    output = (random.randint(tolerance, maxwidth-tolerance), random.randint(100+tolerance, maxheight-tolerance))
    while math.isclose(output[0], char_pos[0], abs_tol=70) or math.isclose(output[1], char_pos[1], abs_tol=70) or math.isclose(output[0], targ_pos[0], abs_tol=70) or math.isclose(output[1], targ_pos[1], abs_tol=70):
        output = (random.randint(tolerance, maxwidth-tolerance), random.randint(100+tolerance, maxheight-tolerance))
    return output

def chance(frequency: Union[int, bool]) -> bool:
    if frequency == False:
        return False
    elif random.random() < 1/frequency:
        return True
    else:
        return False

def minusHeart(hearts: list[bool, bool, bool]) -> list[bool, bool, bool]:
    if hearts[2]:
        hearts[2] = False
    elif hearts[1]:
        hearts[1] = False
    elif hearts[0]:
        hearts[0] = False
    return hearts

def plusHeart(hearts: list[bool, bool, bool]) -> list[bool, bool, bool]:
    if not hearts[1]:
        hearts[1] = True
    elif not hearts[2]:
        hearts[2] = True
    return hearts
