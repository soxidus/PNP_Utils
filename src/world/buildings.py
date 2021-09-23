class Building:
    def __init__(self, name="Derp", rarity=0, cost=1, desc ="Generic Buildiing") -> None:
        self.name = name
        self.rarity = rarity
        self.cost = cost
        self.desc = desc

    def info(self):
            return f'{self.name} {self.rarity} {self.cost} {self.desc} '
    

class SpecialBuilding(Building):
    def __init__(self, name, rarity=2, cost=3, desc ="Generic Special Buildiing") -> None:
        self.name = name
        self.rarity = rarity
        self.cost = cost
        
    def info(self):
        return f'{self.name} {self.rarity} {self.cost} {self.desc} '

class Fortification(Building):
    def __init__(self, name, rarity=1, cost=2, desc ="Generic Fortification") -> None:
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
    "magischer Shop": magicshop,
    "Badehaus": badehaus 
}

d_fortifications = { 
    "Pallisade": pallisade,
    "Graben": graben,
    "Mauer": mauer,
    "Türme": turm,
    "Magischer Schutz": magicprot
} 
