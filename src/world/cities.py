from buildings import Building, SpecialBuilding, Fortification
import buildings
import yaml
from typing import Sized


class City:

    def __init__(self, **kwargs):
        self.__dict__ = dict(kwargs)

    def __init__(self, name="Dummy Stadt", maxSize=5, wealth=10, playerRelation=1.0) -> None:
        self.name = name
        self.maxSize = maxSize
        self.wealth = wealth
        self.playerRelation = 1.0
        self.buildings = [buildings.haus]

    def info(self):
        # print(self.__dict__)
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))


    def fill(self,exhaustWealth=False):         # Todo create randomized city based on wealth, max building count
        if exhaustWealth:
            while self.wealth >0 and len(self.buildings) <= self.maxSize:
                self.buildBuilding()

    def buildBuilding(self, building=buildings.haus, freebie=False):
        if freebie:
            if len(self.buildings) <= self.maxSize:
                self.buildings.append(building) 
        elif building.cost <= self.wealth:
            if len(self.buildings) <= self.maxSize:
                self.buildings.append(building)
                self.wealth =- building.cost
        else:
            return False

    def destroyBuilding(self, building):
        pass

    def info(self):
        # print(self.__dict__)
        print("City Information: ")
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))


class Village(City):
    def __init__(self, name, maxSize, type="village") -> None:
        pass
