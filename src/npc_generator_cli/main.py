from random import choice
from config import Handeln, Wissen, Soziales
from spending import *
from proceeding import *
import inquirer


def main():
    try:
        total_in = int(input("Total number of points to spend or blank for 400: ") or "400")
    except ValueError:
        print("Error!! Got NaN instead of INT")
        exit

    all_q = [
        inquirer.List('choices',
                      message="All Values or Choose some",
                      choices=['all', 'choose'],
                      ),
    ]

    all = inquirer.prompt(all_q)

    if all['choices'] == 'all':
        proceed_all(total_in)

    if all['choices'] == 'choose':
        proceed_selector(total_in)


if __name__ == '__main__':
    main()
