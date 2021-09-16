import builtins
import data
import yaml


class city:

    def __init__(self, **kwargs):
        self.__dict__ = dict(kwargs)

    def __init__(self, name="Dummy Stadt", size=5, wealth=10, playerRelation=1.0) -> None:
        self.name = name
        self.size = size
        self.wealth = wealth
        self.playerRelation = 1.0
        self.buildings = [data.haus]

    def info(self):
        # print(self.__dict__)
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))
        # Todo create randomized city based on wealth, max building count

    def fillCity(self):
        pass

    def advanceCity(self, building):
        if len(self.buildings <= self.size):
            self.buildings.append(building)
        else:
            return False

    def degradeCity(self, building):
        pass


class village(city):
    def __init__(self, name, size, type="village") -> None:
        pass
