
from yaml import load
from world import World
from kingdom import Kingdom
from buildings import Building
import buildings
#import world.faction
import jsonpickle

#todo test

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
#welt.info()
print()
print()
testkingdom = Kingdom("Huberts Bande")
#testkingdom.info()
#print()
#print()
welt.createFaction(testkingdom)
#welt = load_game("test.save")
#welt.info()
print()
print()
#save_game("test.save", welt)
testkingdom.foundCity(True)
welt.info()
print()
print()
testkingdom.cities[0].buildBuilding(buildings.kltempel, True)
#welt.info()
testkingdom.info()
print()
print()
welt.info()
