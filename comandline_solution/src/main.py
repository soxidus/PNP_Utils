from config import Handeln, Wissen, Soziales
from spending import *


def main():
    try:
        total_in = int(input("Total number of points to spend or blank for 400: ") or "400")
    except ValueError:
        print("Error!! Got NaN instead of INT")
        exit
    try:
        dist = int(input("Select distibution \
            1 for Uniform \
            2 for Random \
            ") or "1")
    except ValueError:
        print("Error!! Got NaN instead of INT")
        exit

    if dist == 1:
        spend_all_points_evenly(total_in)
    if dist == 2:
        spend_all_points_random(total_in)

if __name__ == '__main__':
    main()
