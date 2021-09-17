import world.buildings
import yaml
from typing import Sized


class City:

    def __init__(self, **kwargs):
        self.__dict__ = dict(kwargs)

    def __init__(self, name="Dummy Stadt", size=5, wealth=10, playerRelation=1.0) -> None:
        self.name = name
        self.size = size
        self.wealth = wealth
        self.playerRelation = 1.0
        self.buildings = [buildings.haus]

    def info(self):
        # print(self.__dict__)
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))
        # Todo create randomized city based on wealth, max building count

    def fill(self):
        pass

    def advance(self, building, freebie=False):
        if freebie:
            if len(self.buildings <= self.size):
                self.buildings.append(building) 
        elif building.cost < self.wealth:
            if len(self.buildings <= self.size):
                self.buildings.append(building) 
        else:
            return False


    def degrade(self, building):
        pass

    def info(self):
        # print(self.__dict__)
        print("City Information: ")
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))


class village(City):
    def __init__(self, name, size, type="village") -> None:
        pass
