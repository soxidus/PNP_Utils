from yaml import load
from world.world import World
import jsonpickle

print("Test Bed for Faction and Worldmanagement")


def save_game(filename, world):
    with open(filename, 'w') as savegame:
        savegame.write(jsonpickle.encode(world))


def load_game(filename):
    with open(filename, 'r') as savegame:
        world = jsonpickle.decode(savegame.read())
    return world


# welt = World("Glynnmouth")
welt = load_game("test.save")
welt.info()
#save_game("test.save", welt)
