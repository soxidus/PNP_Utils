from config import Handeln, Wissen, Soziales
from spending import spend_all_points


def main():
    print(Handeln)
    try:
        total_in = int(input("Total number of points to spend or blank for 400: ") or "400")
        print(total_in)
    except ValueError:
        print("Error!! Got NaN instead of INT")
        exit
    spend_all_points(total_in)


if __name__ == '__main__':
    main()
