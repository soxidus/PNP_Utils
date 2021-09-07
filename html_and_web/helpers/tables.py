# import things
import os, sys
import pandas as pd
import numpy as np


currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from config import Handeln, Soziales, Wissen
# import things
#from flask_table import Table, Col
#
## Declare your table
#class ItemTable(Table):
#    name = Col('Name')
#    description = Col('Description')
#
## Get some objects
#class Item(object):
#    def __init__(self, name, description):
#        self.name = name
#        self.description = description
#items = [Item('Name1', 'Description1'),
#         Item('Name2', 'Description2'),
#         Item('Name3', 'Description3')]
#
## Or, more likely, load items from your database with something like
#items = ItemModel.query.all()
#
## Populate the table
#table = ItemTable(items)
#
## Print the html
#print(table.__html__())
## or just {{ table }} from within a Jinja template


def parse_array(in1, in2, in3):
    max_array_len = max(len(in1), len(in2), len(in3))
    new_array = []

    for i in range(max_array_len):
        try:
            new_array[i][0] = in1
        except IndexError:
            continue
        try:
            new_array[i][1] = in2
        except IndexError:
            continue
        try:
            new_array[i][2] = in3
        except IndexError:
            continue

    return new_array


def distribute_points(points, field):
    pass


def display_table(in_array):

    pass
    return 0


nh = np.array(Handeln, dtype=object)
nw = np.array(Wissen, dtype=object)
ns = np.array(Soziales, dtype=object)
a = np.array((Handeln, Wissen, Soziales), dtype=object)


#print(Handeln)

#print(np.matrix(parse_array(Handeln, Wissen, Soziales)))
