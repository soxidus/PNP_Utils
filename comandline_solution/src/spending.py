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


def spend_all_points_random(total):

    sum_fields = len(Handeln)
    sum_fields += len(Wissen)
    sum_fields += len(Soziales)
    
    remaining = total

    for i in Handeln:
        points_to_spend = randomize_points_with_range(remaining)
        print(match_val_to_text(i, points_to_spend))
        remaining -= points_to_spend

    for i in Wissen:
        points_to_spend = randomize_points_with_range(remaining)
        print(match_val_to_text(i, points_to_spend))
        remaining -= points_to_spend

    for i in Soziales:
        points_to_spend = randomize_points_with_range(remaining)
        print(match_val_to_text(i, points_to_spend))
        remaining -= points_to_spend
