

from typing import Sized
import yaml
import json
from types import SimpleNamespace


class World:
    def __init__(self, name, size=10, count=5) -> None:
        self.name = name
        self.size = size
        self.factioncount = count
        self.faction = {} 


    def info(self):
        # print(self.__dict__)
        print(yaml.dump(self.__dict__, default_flow_style=False, sort_keys=False))