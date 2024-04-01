from Class.Carte.Paquet import Paquet
from Class.Joueur.Joueur import Joueur


class Jeu:

    def __init__(self, nb_Joueur, nb_Carte):
        if 3 <= nb_Joueur <= 5:
            self.nb_Joueur = nb_Joueur
        else:
            raise ValueError("Le nombre de joueurs doit être compris entre 3 et 5.")
        self.nb_Carte = nb_Carte
        self.joueurs = []

    def define_nb_Joueur(Null):
        while True:
            try:
                nb_Joueur = int(input("Entrez le nombre de joueurs (3 à 5): "))
                if 3 <= nb_Joueur <= 5:
                    break
                else:
                    print("Le nombre de joueurs doit être compris entre 3 et 5.")
            except ValueError:
                print("Veuillez entrer un nombre entier.")

        return nb_Joueur

    def define_nb_Carte(Null):
        while True:
            try:
                nb_Carte = int(input("Entrez le nombre de cartes par joueur: "))
                if nb_Carte > 0:
                    break
                else:
                    print("Le nombre de cartes doit être supérieur à 0.")
            except ValueError:
                print("Veuillez entrer un nombre entier.")

        return nb_Carte

    def get_nom(nb_Joueur):
        listNom = []
        for i in range(nb_Joueur):
            nom = input(f"Entrez le nom du joueur {i+1}: ")
            listNom.append(nom)

        return listNom

    def initialisation(self):
        pack = Paquet()
        pack.melanger()
        pack.couper()

        noms = Jeu.get_nom(self.nb_Joueur)

        self.joueurs = []

        for i in range(self.nb_Joueur):
            joueur = Joueur(i, noms[i], [])
            self.joueurs.append(joueur)

            lot = pack.distribuer(1, self.nb_Carte)
            for carte in lot[0]:
                joueur.main.append(carte)

        for i, joueur in enumerate(self.joueurs, start=1):
            print(joueur)

    def tour(self):
        for joueur in self.joueurs:
            print("##########################################")
            print(f"# Tour du joueur {joueur.nom} #")
            print(joueur)
            print("########################################## \n")

            choix = input("Choisissez une, 2, ou 3 de vos cartes avec un chiffre, ou faite pass avec 'p', ou 'q' pour quitter")
            if choix.lower() == 'q':
                print(f"Jeu interrompu par {joueur.nom}.")
                exit(0)
            elif choix.lower() == 'p':
                joueur.passer()
            else:
                pass


    def verif_fin_jeu(self):
        nb_joueurs_avec_cartes = 0
        for joueur in self.joueurs:
            if joueur.nb_Carte_En_Main() > 0:
                nb_joueurs_avec_cartes += 1

        return nb_joueurs_avec_cartes >= 2


    def jeu(self):
        while self.verif_fin_jeu():
            print("##########################################")
            print("#             DEBUT DU JEU               #")
            print("##########################################\n")
            self.tour()



