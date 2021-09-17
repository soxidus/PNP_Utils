import faction
import cities
import buildings
from typing import Sized
import yaml


class World:
    def __init__(self, name, maxfactions=5) -> None:
        self.worldname = name
        self.maxfactions = maxfactions
        self.countfactions = 0
        self.factions = []


    def createFaction(self, faction):
        if self.countfactions <= self.maxfactions:
            self.factions.append(faction)
            self.countfactions += 1
        else:
            return False

    def loadfaction(self, file):
        pass

    def deleteFaction(self, faction):
        pass

    def info(self):
        # print(self.__dict__)
        print("Worldinformation: ")
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))