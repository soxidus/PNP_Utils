import math
from config import Handeln, Wissen, Soziales


def spend_all_points(total):
    sum_fields = len(Handeln)
    sum_fields += len(Wissen)
    sum_fields += len(Soziales)

    points_per_field = math.floor(total / sum_fields)
    bonus_points = total % sum_fields

    print(points_per_field)

