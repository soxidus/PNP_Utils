import yaml


class Faction: 
    "Template Faction"

    def __init__(self, name, race, wealth, relationToPlayer=1.0) -> None:
        pass


def info(self):
        # print(self.__dict__)
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))
