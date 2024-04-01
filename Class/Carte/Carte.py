class Carte:

    symbolValide = ("\u2663", "\u2665", "\u2666", "\u2660")
    valeurValide = tuple(list(range(1,11))+["VALET","DAME", "ROI"])

    # Constructor
    def __init__(self, val, symbol, puissance, position):
        self.val = val
        self.symbol = symbol
        self.puissance = puissance
        self.position = position

    def points(self):
        return Carte.valeurValide.index(self.val)+1

    def couleur(self):
        return self.symbol

    def get_puissance(self):
        return self.puissance

    def attribut_puissance(val):
        match val:
            case "VALET":
                puissance = 11
            case "DAME":
                puissance = 12
            case "ROI":
                puissance = 13
            case 2:
                puissance = 14
            case _:
                puissance = val
        return puissance


    def __repr__(self):
        return f"Carte : {self.val}{self.symbol} Puissance = {self.puissance} ({self.position})"