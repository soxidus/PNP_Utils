import yaml


class Faction: 
    
    def __init__(self, name="Dummy Faction", race="Human", cityCount=3, playerRelation=1.0) -> None:
        self.name = name
        self.race = race
        self.cityCount = cityCount
        self.playerRelation = 1.0
        # self.buildings = [data.haus]

    def fillCity(self, wealth)
        pass


def info(self):
    # print(self.__dict__)
    print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))
