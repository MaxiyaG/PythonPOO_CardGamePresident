"""
File : Carte.py
Description : Ce fichier définit la classe Carte, qui représente une carte.
              Chaque carte a une valeur, un symbole, une puissance et une position.
Author : GUNDUZ Maxime / M'PEMBELE Dieuleveut / GUEDJALI Aniss
Date : 28/04/2024
"""
class Carte:

    symbolValide = ("\u2663", "\u2665", "\u2666", "\u2660")
    valeurValide = tuple(list(range(1,11))+["VALET","DAME", "ROI"])

    # Constructor
    def __init__(self, val, symbol, puissance, position):
        """
        Constructeur de la classe Carte.
        Initialise une carte avec une valeur, un symbole, une puissance et une position.
        """
        self.val = val
        self.symbol = symbol
        self.puissance = puissance
        self.position = position

    def attribut_puissance(val):
        """
        Méthode pour attribuer une puissance à une carte en fonction de sa valeur.
        Les cartes spéciales (Valet, Dame, Roi, As et 2) ont des puissances supérieures aux cartes numériques.
        """
        match val:
            case "VALET":
                puissance = 11
            case "DAME":
                puissance = 12
            case "ROI":
                puissance = 13
            case 1:
                puissance = 14
            case 2:
                puissance = 15
            case _:
                puissance = val
        return puissance

    def __repr__(self):
        """
        Méthode pour représenter une carte sous forme de chaîne de caractères.
        Affiche la valeur, le symbole, la puissance et la position de la carte.
        """
        return f" {self.val}{self.symbol} | Puissance = {self.puissance} | => (Position = {self.position})"