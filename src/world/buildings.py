class Building:
    def __init__(self, name="Derp", rarity=0, cost=1) -> None:
        self.name = name
        self.rarity = rarity
        self.cost = cost

        def info(self):
            return f'{self.rarity} {self.name}, value {self.value}'
    

class SpecialBuilding(Building):
    def __init__(self, name, rarity=2, cost=3) -> None:
        self.name = name
        self.rarity = rarity
        self.cost = cost


class Fortification(Building):
    def __init__(self, name, rarity=1, cost=2) -> None:
        self.name = name
        self.rarity = rarity
        self.cost = cost


# normale Gebäude
haus = Building("Wohnviertel", 0, 0)
kltempel = Building("kl. Tempel", 1, 1)
schmiede = Building("Schmiede", 0, 1)

# special_buildings
magicshop = Building("magischer Shop", 3, 4)
badehaus = SpecialBuilding("Badehaus", 2, 2)

# fortifications
pallisade = Fortification("Pallisade", 1, 1)
graben = Fortification("Graben", 1, 1)
mauer = Fortification("Mauer", 1, 3)
turm = Fortification("Türme", 2, 2)
magicprot = Fortification("Magischer Schutz", 3, 5)

# Dictonary with all Buildings for easy acces
d_buildings = {
    "Wohnviertel": haus,
    "kl. Tempel": kltempel,
    "Schmiede": schmiede
} 
d_specialBuildings = { 

}

d_fortifications = { 
    "Pallisade": pallisade,
    "Graben": graben,
    "Mauer": mauer,
    "Türme": turm,
    "Magischer Schutz": magicprot
} 
