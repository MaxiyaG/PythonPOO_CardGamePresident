"""
File : Paquet.py
Description : Ce fichier définit la classe Paquet, qui représente un paquet de cartes.
              Chaque paquet peut être mélangé, coupé, et des cartes peuvent être piochées et distribuées.
Author : GUNDUZ Maxime / M'PEMBELE Dieuleveut / Aniss
Date : 28/04/2024
"""

from Class.Carte.Carte import Carte
import random

class Paquet(Carte):

    # Constructor
    def __init__(self):
        """
        Constructeur de la classe Paquet.
        Initialise un paquet avec toutes les cartes.
        """

        self.listCard = []

        for symbol in Carte.symbolValide:
            for val in Carte.valeurValide:

                puissance = Carte.attribut_puissance(val)

                c = Carte(val, symbol, puissance, position=None)
                Carte.__repr__(c)
                self.listCard.append(c)

    def __repr__(self):
        """
        Méthode pour représenter un paquet sous forme de chaîne de caractères.
        Affiche toutes les cartes dans le paquet.
        """
        return str(self.listCard)


    def melanger(self):
        """
        Méthode pour mélanger le paquet de cartes.
        """
        random.shuffle(self.listCard)


    def couper(self):
        """
        Méthode pour couper le paquet de cartes.
        Le paquet est coupé à un index aléatoire et les deux moitiés sont inversées.
        """

        n = random.randint(1,len(self.listCard))
        x = []
        y = []

        for i in self.listCard:
            if self.listCard.index(i) < n : 
                x.append(i)
            else:
                y.append(i)
        
        self.listCard = y + x
        
        return self.listCard


    def pioche(self):
        """
        Méthode pour piocher la carte en haut du paquet.
        Retourne la carte piochée et la supprime du paquet.
        """

        carte_pioche = self.listCard[0]
        self.listCard.pop(0)
        return carte_pioche

    def distribuer(self, nb_Joueur, nb_Carte):
        """
        Méthode pour distribuer les cartes aux joueurs.
        Distribue un nombre spécifié de cartes à un nombre spécifié de joueurs.
        Retourne une liste de listes de cartes, chaque sous-liste représentant la main d'un joueur.
        """

        distribution = [[] for i in range(0, nb_Joueur)]

        for i in range(0, nb_Carte):
            for j in range(0, nb_Joueur):
                carte = self.pioche()
                carte.position = i + 1
                distribution[j].append(carte)

        return distribution
