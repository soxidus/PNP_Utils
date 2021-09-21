import yaml
from typing import Sized
from cities import City, Village
from buildings import Building, SpecialBuilding, Fortification


class Faction:
    def __init__(self, name="Dummy Faction", race="Human", maxCities=3, playerRelation=1.0, wealth=10) -> None:
        self.name = name
        self.race = race
        # self.cityCount = 0 # Done via Length of city array
        self.maxCities = maxCities
        self.playerRelation = 1.0
        self.wealth = wealth
        self.cities = []
        self.relations = {}
        # self.buildings = [data.haus]

    def foundCity(self, freebie, city=City()):
        if freebie:
            if len(self.cities) <= self.maxCities:
                self.cities.append(city) 


    def destroyCity(self):
        pass

    def info(self):
        # print(self.__dict__)
        print("Factionsinfo: ")
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))
