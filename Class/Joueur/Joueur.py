"""
File : Joueur.py
Description : Ce fichier définit la classe Joueur, qui représente un joueur.
              Chaque joueur a un numéro, un nom et une main de cartes.
Author : MaxiyaG
Date : 28/04/2024
"""

class Joueur:

    def __init__(self, numero, nom, main):
        """
        Constructeur de la classe Joueur.
        Initialise un joueur avec un numéro, un nom et une main de cartes.
        """
        self.numero = numero
        self.nom = nom
        self.main = []

    def nb_Carte_En_Main(self):
        """
        Méthode pour obtenir le nombre de cartes dans la main du joueur.
        Retourne le nombre de cartes dans la main du joueur.
        """
        return len(self.main)

    def __repr__(self):
        """
        Méthode pour représenter un joueur sous forme de chaîne de caractères.
        Affiche le nom du joueur et les cartes dans sa main.
        """
        self.main = sorted(self.main, key=lambda carte: carte.puissance)
        for i, carte in enumerate(self.main):
            carte.position = i + 1
        return f"Joueur {self.nom} :\n" + "\n".join(f"{carte})" for i, carte in enumerate(self.main))
