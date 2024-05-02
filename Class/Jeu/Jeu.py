"""
File : Jeu.py
Description : Ce fichier définit la classe Jeu, qui représente le jeu du Président.
              Chaque instance de Jeu gère le déroulement d'une partie, y compris l'initialisation du jeu,
              la définition du nombre de joueurs et de cartes, la gestion des tours et la vérification de la fin du jeu.
Author : GUNDUZ Maxime / M'PEMBELE Dieuleveut / GUEDJALI Aniss
Date : 28/04/2024
"""

from Class.Carte.Paquet import Paquet
from Class.Jeu.Tour import Tour
from Class.Joueur.Joueur import Joueur


class Jeu:
    nb_carte_autorise = None
    premierJoueur = True

    def __init__(self, reGame=False, tabWin=None, nb_Joueur=None, nb_Carte=None, listNom=None):
        """
        Constructeur de la classe Jeu.
        Initialise une instance de Jeu avec des paramètres optionnels pour une nouvelle partie ou une partie en cours.
        """

        self.reGame = reGame
        self.nb_tour = 1
        self.previous_coup = None

        if reGame is False:
            self.introduction()
            nb_Joueur = self.define_nb_Joueur()
            nb_Carte = self.define_nb_Carte(nb_Joueur)
            self.tabWin = []
            self.tabNom = []

        else:
            self.tabNom = listNom
            self.tabWin = tabWin
            self.nb_Joueur = nb_Joueur
            self.nb_Carte = nb_Carte


        self.dernierAvoirJouer = None
        self.passage_succesif = 0

        if 3 <= nb_Joueur <= 5:
            self.nb_Joueur = nb_Joueur
        else:
            raise ValueError("Le nombre de joueurs doit être compris entre 3 et 5.")
        self.nb_Carte = nb_Carte
        self.joueurs = []

        self.initialisation()

    def introduction(self):
        """
        Méthode pour afficher une introduction au jeu, expliquant les règles et demandant aux joueurs s'ils sont prêts à jouer.
        """

        print("\n##########################################")
        print("# Bienvenue dans le jeu du President ! #")
        print("##########################################\n")

        print("- Le président :\n")
        print("Il se joue à plusieurs (de 3 à 5 joueurs).\n"
              "C’est un jeu de défausse en plusieurs manches,\n"
              "le gagnant est le premier qui n’a plus de carte en main à la fin de la manche,\n"
              "il devient \"Président\"\n"
              "(Pour la seconde manche et pourra choisir 2 cartes à donner à un autre joueur)\n")

        print("##########################################\n")

        print("- L’ordre des cartes :\n")
        print("Il est un peu différent qu’à l’habitude. La meilleure carte est le 2,\n"
              " puis l’ordre plus classique : As, roi, dame, valet, 10, 9, 8… \n"
              "(facultatif : celui qui a la dame de cœur dans son jeu commence avec la carte de son choix).\n")

        print("##########################################\n")

        print("- Les règles du jeu :\n")
        print("Chacun son tour, les joueurs doivent poser une carte,\n"
              " on ne peut que monter sur la carte précédente ou mettre exactement la même.\n"
              " La fin du pli est lorsque plus personne ne peut jouer.\n"
              " Les cartes sont alors écartées et le dernier joueur à avoir posé une carte peut démarrer un nouveau tour.\n"
              " Par exemple, sur un 5, on peut soit mettre une carte plus forte, soit un autre 5.\n"
              " Dans ce cas, le joueur d’après ne pourra plus monter,\n"
              " il devra soit mettre un cinq également, soit passer son tour.\n"
              "Le premier joueur a aussi la possibilité de poser directement un double ou un triple.\n"
              " Dans ce cas, les joueurs suivants doivent également soit mettre un double identique, \n"
              "soit monter avec des doubles ou triples plus forts.\n"
              " Le 2 ferme systématiquement le tour de jeu (on ne peut pas poser un 2 sur un 2).\n"
              " Celui qui l’a posé, reprend la main pour un nouveau tour.\n")

        print("##########################################\n")

        print("- Développeur (2024) :")
        print("- GUNDUZ Maxime\n"
              "- M'PEMBELE Dieuleveut\n"
              "- Aniss\n"
              "Sous la supervision de l'université Sorbonne Paris Nord par Mme MARIN Julie (enseignante)\n")

        while True:
            print("##########################################")
            pret = input("Êtes-vous prêt à jouer au Jeu du président ? (o = Oui/ n = Non): ")
            print("##########################################\n")
            if pret.lower() == 'o' or pret.lower() == 'oui':
                return
            elif pret.lower() == 'n' or pret.lower() == 'non':
                print("\nAu revoir\n")
                exit(0)
            else:
                print("Veuillez entrer 'o' pour oui ou 'n' pour non.\n")

    def define_nb_Joueur(self):
        """
        Méthode pour définir le nombre de joueurs en demandant à l'utilisateur d'entrer un nombre entre 3 et 5.
        """

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

    def permute_carte(self):
        """
        Méthode pour permuter les cartes entre le gagnant et le perdant de la dernière partie.
        """

        winner = self.tabWin[0].nom
        loser = self.tabWin[-1].nom

        # Trouver les correspondants dans self.joueurs et self.tabWin avec les noms
        winner_player = next((player for player in self.joueurs if player.nom == winner), None)
        loser_player = next((player for player in self.joueurs if player.nom == loser), None)

        print("Le joueur", winner_player.nom, "a échangé des cartes avec le joueur", loser_player.nom)

        if not winner_player.main or not loser_player.main:
            print("L'un des joueurs n'a aucune cartes dans sa main")
            return

        loser_max = max(loser_player.main, key=lambda carte: carte.puissance)
        winner_max = min(winner_player.main, key=lambda carte: carte.puissance)

        # Afficher les cartes permutées
        print("Carte échangée du perdant (", loser_player.nom, "):", loser_max)
        print("Carte échangée du gagnant (", winner_player.nom, "):", winner_max)

        loser_player.main.remove(loser_max)
        winner_player.main.remove(winner_max)
        loser_player.main.append(winner_max)
        winner_player.main.append(loser_max)

        self.tabWin = []

    def define_nb_Carte(self, nb_Joueur):
        """
        Méthode pour définir le nombre de cartes par joueur en demandant à l'utilisateur d'entrer un nombre.
        """

        while True:
            try:
                max_cartes = int(52 / nb_Joueur)
                nb_Carte = int(input(
                    "Entrez le nombre de cartes par joueur (Vous pouvez au maximum mettre {0}): ".format(max_cartes)))

                if nb_Carte > 0 and nb_Carte <= max_cartes:
                    break
                elif nb_Carte > max_cartes:
                    print("Nous avons seulement 52 cartes disponibles.")
                else:
                    print("Le nombre de cartes doit être supérieur à 0.")
            except ValueError:
                print("Veuillez entrer un nombre entier.")

        return nb_Carte

    def get_nom(nb_Joueur):
        """
        Méthode pour obtenir les noms des joueurs en demandant à l'utilisateur d'entrer un nom pour chaque joueur.
        """

        listNom = []
        for i in range(nb_Joueur):
            nom = ""
            while not nom.strip():
                nom = input(f"Entrez le nom du joueur {i + 1}: ")
                if not nom.strip():
                    print("Le nom ne peut pas être vide. Veuillez réessayer.")
            listNom.append(nom.strip())
        return listNom

    def initialisation(self):
        """
        Méthode pour initialiser le jeu en créant un paquet de cartes, en mélangeant et en coupant le paquet,
        et en distribuant les cartes aux joueurs.
        """

        pack = Paquet()
        pack.melanger()
        pack.couper()

        if self.reGame is False:
            noms = Jeu.get_nom(self.nb_Joueur)
        else:
            noms = self.tabNom

        self.joueurs = []

        for i in range(self.nb_Joueur):
            joueur = Joueur(i, noms[i], [])
            self.joueurs.append(joueur)

            if self.reGame is False:
                self.tabNom.append(joueur.nom)

            lot = pack.distribuer(1, self.nb_Carte)
            for carte in lot[0]:
                joueur.main.append(carte)

        if self.reGame:
            self.permute_carte()

    def tour(self):
        """
        Méthode pour gérer un tour de jeu, où chaque joueur joue un coup.
        """

        tabActif = []
        previous_coup = None
        for i, joueur in enumerate(self.joueurs):

            if len(self.joueurs) == 1:
                self.tabWin.append(self.joueur)
                return

            if joueur in self.tabWin:
                continue

            print("##########################################")
            print(f"# Tour du joueur {joueur.nom} #")
            if joueur.nb_Carte_En_Main() > 0:
                print(f"Le joueur {joueur.nom} a des cartes dans sa main.")
            else:
                print(f"Le joueur {joueur.nom} n'a pas de cartes dans sa main.")
                if joueur not in self.tabWin:
                    self.tabWin.append(joueur)
                   # self.passage_succesif = len(self.jeu.joueurs) - len(self.jeu.tabWin)
                continue
            print(joueur)
            print("########################################## \n")

            if i != 0:
                nombre_cartes_autorise = self.nb_carte_autorise
            else:
                nombre_cartes_autorise = None

            tour = Tour(self, joueur, nombre_cartes_autorise)
            coup = tour.saisir_coup(self.previous_coup)

            if coup is not None and coup != self.previous_coup:
                self.previous_coup = coup
                self.dernierAvoirJouer = joueur
                if i == 0:
                    self.nb_carte_autorise = len(coup)
            else:
                if i == 0:
                    self.nb_carte_autorise = None

            tabActif.append(coup)

        self.nb_tour += 1

        return tabActif

    def rejouer(self):
        """
        Méthode pour demander aux joueurs s'ils veulent rejouer une fois le jeu terminé.
        """

        while True:
            choix = input("Voulez-vous rejouer ? (o/n): ")
            if choix.lower() == 'o':
                return True
            elif choix.lower() == 'n':
                return False
            else:
                print("Veuillez entrer 'o' pour oui ou 'n' pour non.")

    def print_classement(self):
        """
        Méthode pour afficher le classement final des joueurs à la fin du jeu.
        """

        print("\nClassement final des joueurs :")
        for i, joueur in enumerate(self.tabWin):
            if i == 0:
                print(f"Le President est {joueur.nom} !")
            elif i == len(self.tabWin) - 1:
                print(f"Le Paysan est {joueur.nom}.")
            else:
                print(f"{i + 1}. {joueur.nom}")

    def jeu(self):
        """
        Méthode pour démarrer le jeu et gérer le déroulement du jeu jusqu'à ce qu'il se termine.
        """

        while True:

            print("##########################################")
            print("#             DEBUT DU JEU               #")
            print("##########################################\n")

            while len(self.tabWin) < len(self.joueurs) - 1:
                self.tour()

            # Ajoute le dernier joueur restant à tabWin et le supprime de self.joueurs
            for joueur in self.joueurs:
                if joueur not in self.tabWin:
                    self.tabWin.append(joueur)
                    self.joueurs.remove(joueur)

            # Affiche le classement final des joueurs après la fin du jeu
            self.print_classement()

            # Demande à l'utilisateur s'il veut rejouer
            if not self.rejouer():
                print("\nAu revoir\n")
                break

            self.__init__(reGame=True, tabWin=self.tabWin, nb_Joueur=self.nb_Joueur, nb_Carte=self.nb_Carte,listNom=self.tabNom)