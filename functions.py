import math, random

def time_to_minutes(time):
    minutes = str(time//60)
    seconds = time % 60
    seconds = f"{seconds:02d}"
    return minutes+":"+seconds

def random_pos(tolerance, maxwidth, maxheight, char_pos=(-1000, -1000), targ_pos=(-1000, -1000)):
    output = (random.randint(tolerance, maxwidth-tolerance), random.randint(100+tolerance, maxheight-tolerance))
    while math.isclose(output[0], char_pos[0], abs_tol=70) or math.isclose(output[1], char_pos[1], abs_tol=70) or math.isclose(output[0], targ_pos[0], abs_tol=70) or math.isclose(output[1], targ_pos[1], abs_tol=70):
        output = (random.randint(tolerance, maxwidth-tolerance), random.randint(100+tolerance, maxheight-tolerance))
    return output

def regen_chance(frequency):
    if frequency == False:
        return False
    elif random.random() < 1/frequency:
        return True
    else:
        return False

def minusHeart(hearts):
    if hearts[2]:
        hearts[2] = False
    elif hearts[1]:
        hearts[1] = False
    elif hearts[0]:
        hearts[0] = False
    return hearts

def plusHeart(hearts):
    if not hearts[1]:
        hearts[1] = True
    elif not hearts[2]:
        hearts[2] = True
    return hearts
