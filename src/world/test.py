
from yaml import load
from world import World
from faction import Faction
import buildings
#import world.faction
import jsonpickle

print("Test Bed for Faction and Worldmanagement")
print()

def save_game(filename, world):
    with open(filename, 'w') as savegame:
        savegame.write(jsonpickle.encode(world))


def load_game(filename):
    with open(filename, 'r') as savegame:
        world = jsonpickle.decode(savegame.read())
    return world


welt = World("Glynnmouth")
testfaction = Faction("Huberts Bande")
testfaction.info()
print()
print()
welt.createFaction(testfaction)
#welt = load_game("test.save")
welt.info()
print()
#save_game("test.save", welt)
#testfaction.foundCity


