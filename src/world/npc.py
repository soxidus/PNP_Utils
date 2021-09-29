import math


class NPC:
    def __init__(self, name="Dummy NPC", race="Human",playerRelation=1.0, descr="Dummy", cp=400) -> None:
        self.name = name
        self.race = race
        self.playerRelation = 1.0
        self.descr = descr
        self.notes 
        self.hp
        self.Handeln = {}
        self.Wissen = {} 
        self.Soziales ={} 

    def spendPoints(self, points):
        pass

    def spendPointsUniform(self, points):
        sum_fields = len(Handeln)
        sum_fields += len(Wissen)
        sum_fields += len(Soziales)
        points_per_field = math.floor(points / sum_fields)

        bonus_points = points % sum_fields



# Set global NPC params here
Handeln = [
    "Nahkampf",
    "Fernkampf",
    "Einhand Waffen",
    "Zweihand Waffen",
    "Hiebwaffen",
    "Agilität (Springen Klettern und Co.)",
    "Schlossknacken",
    "Taschendiebstahl",
    "Verstecken",
    "Schleichen",
    "Erste Hilfe (Benötigt Mats)",
    "Angeln",
    "Tanzen",
    "Reiten",
    "Kraft"
    ]
Wissen = [
    "Magie",
    "Geschichte und Mythen",
    "Tierkunde",
    "Pflanzenkunde",
    "Gesteinskunde",
    "Geographie",
    "Medizin",
    "Kochen",
    "Alchemie",
    "Fremdsprachen",
    "Gesellschaft / Allgemeinwissen",
    "Lesen / Schreiben",
    "Wahrnehmung"
    ]
Soziales = [
    "Lügen",
    "Überzeugen",
    "Verhandeln",
    "Einschüchtern",
    "Menschenkenntnis",
    "Betören",
    "Beruhigen",
    "Redegewandtheit",
    "Humor",
    "Zechen",
    "Begeistern",
    "Ablenken",
    "Manipulation"
    ]



