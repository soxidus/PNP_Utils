import math
import random
from config import Handeln, Wissen, Soziales
from visualization import match_val_to_text

def spend_all_points_evenly(total):
    sum_fields = len(Handeln)
    sum_fields += len(Wissen)
    sum_fields += len(Soziales)

    points_per_field = math.floor(total / sum_fields)
    bonus_points = total % sum_fields

    print(points_per_field)
    for i in Handeln:
        print(match_val_to_text(i, points_per_field))
    for i in Wissen:
        print(match_val_to_text(i, points_per_field))
    for i in Soziales:
        print(match_val_to_text(i, points_per_field))

def randomize_points_with_range(remaining):
    if remaining < 100:
        rand_points = random.randint(0,remaining)
    else:
        rand_points = random.randint(0,100)
    
    return rand_points


def spend_bonus(total, a, b, c):
    bonus = total - a - b - c
    selector = random.randint(1,3)
    
    if selector == 1:
        return a + bonus, b, c
    if selector == 2:
        return a, b + bonus, c
    if selector == 3:
        return a, b, c + bonus
    else:
        return a, b, c

def spend_all_points_random(total):

    sum_fields = len(Handeln)
    sum_fields += len(Wissen)
    sum_fields += len(Soziales)
    
    remaining_h = math.floor(total /3)
    remaining_w = math.floor(total /3)
    remaining_s = math.floor(total /3)

    remaining_h,remaining_w,remaining_s = spend_bonus(total, remaining_h, remaining_w, remaining_s)

    print()
    print("Handeln:")
    for i in Handeln:
        points_to_spend = randomize_points_with_range(remaining_h)
        print(match_val_to_text(i, points_to_spend))
        remaining_h -= points_to_spend

    print()
    print("Wissen:")
    for i in Wissen:
        points_to_spend = randomize_points_with_range(remaining_w)
        print(match_val_to_text(i, points_to_spend))
        remaining_w -= points_to_spend

    print()
    print("Soziales:")
    for i in Soziales:
        points_to_spend = randomize_points_with_range(remaining_s)
        print(match_val_to_text(i, points_to_spend))
        remaining_s -= points_to_spend
