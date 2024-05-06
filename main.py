"""
File : main.py
Description : Ce code crée une instance de la classe Jeu à partir du module Jeu.
Author : GUNDUZ Maxime 
Date : 28/04/2024
"""

from Class.Jeu.Jeu import Jeu

if __name__ == "__main__":
    try:
        jeu = Jeu()
        jeu.jeu()
    except Exception as e:
        print(f"Une erreur innatendu est survenu : {e}")
