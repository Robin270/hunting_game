import random

def time_to_minutes(time):
    minutes = str(time//60)
    seconds = time % 60
    seconds = f"{seconds:02d}"
    output = minutes+":"+seconds
    return output

# def random_target_pos(maxwidth, maxheight)