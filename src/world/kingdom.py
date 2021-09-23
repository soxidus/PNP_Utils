import yaml
from typing import Sized
from cities import City, Village
from buildings import Building, SpecialBuilding, Fortification


class Kingdom:
    def __init__(self, name="Dummy Kingdom", race="Human", maxCities=3, playerRelation=1.0, wealth=10) -> None:
        self.name = name
        self.race = race
        # self.cityCount = 0 # Done via Length of city array
        self.maxCities = maxCities
        self.playerRelation = 1.0
        self.wealth = wealth
        self.cities = []
        self.relations = {}

    def foundCity(self, freebie=True, city=City()):
        if len(self.cities) <= self.maxCities:
            if freebie:
                self.cities.append(city) 
            else:
                if self.wealth > 10:
                    self.wealth -= 50
                    self.cities.append(city) 

    def growCity(self, value=1):
        self.maxCities += value




    def destroyCity(self):
        pass

    def info(self):
        # print(self.__dict__)
        print("Kingdomsinfo: ")
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))
