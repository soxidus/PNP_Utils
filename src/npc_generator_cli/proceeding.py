from random import choice
from config import Handeln, Wissen, Soziales
from spending import *
import inquirer


def proceed_all(total_in):
    dist_q = [
        inquirer.List('choice',
                      message="Select distibution",
                      choices=['Uniform', 'Random'],
                      ),
    ]
    dist = inquirer.prompt(dist_q)

    if dist['choice'] == 'Uniform':
        spend_all_points_evenly(total_in, Handeln, Wissen, Soziales)
    if dist['choice'] == 'Random':
        spend_all_points_random(total_in, Handeln, Wissen, Soziales)


def proceed_selector(total_in):

    handeln_q = [
        inquirer.Checkbox('choices',
                          message="Select Values from Handeln",
                          choices=Handeln,
                          ),
    ]
    handeln_v = inquirer.prompt(handeln_q)['choices']

    wissen_q = [
        inquirer.Checkbox('choices',
                          message="Select Values from Wissen",
                          choices=Wissen,
                          ),
    ]
    wissen_v = inquirer.prompt(wissen_q)['choices']

    soziales_q = [
        inquirer.Checkbox('choices',
                          message="Select Values from Soziales",
                          choices=Soziales,
                          ),
    ]
    soziales_v = inquirer.prompt(soziales_q)['choices']

    dist = select_distribution()

    if dist['choice'] == 'Uniform':
        spend_all_points_evenly(total_in, handeln_v, wissen_v, soziales_v)
    if dist['choice'] == 'Random':
        spend_all_points_random(total_in, handeln_v, wissen_v, soziales_v)


def select_distribution():
    dist_q = [
        inquirer.List('choice',
                      message="Select distibution",
                      choices=['Uniform', 'Random'],
                      ),
    ]
    dist = inquirer.prompt(dist_q)
    return dist
