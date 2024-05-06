"""
File : Tour.py
Description : Ce fichier définit la classe Tour, qui représente un tour dans le jeu.
              Chaque instance de Tour gère le déroulement d'un tour, y compris la vérification de la victoire,
              Cette instance gére la saisie d'un coup d'un joueur.
Author : MaxiyaG
Date : 28/04/2024
"""
from Class.Joueur.Joueur import Joueur

class Tour:

    def __init__(self, jeu, joueur, nb_carte_autorise=None, premierJoueur=False):
        """
        Constructeur de la classe Tour.
        Initialise un tour avec le jeu en cours, le joueur actuel, le nombre de cartes autorisées et un indicateur pour le premier joueur.
        """

        self.jeu = jeu
        self.joueur = joueur
        self.nb_carte_autorise = nb_carte_autorise
        self.premierJoueur = premierJoueur

    def check_doublon(self, tabCoup):
        """
        Méthode pour vérifier si le coup contient des doublons.
        Retourne True si aucun doublon n'est trouvé, False sinon.
        """

        return len(tabCoup) == len(set(tabCoup))

    def validate_coup(self, selected_cards, previous_coup):
        """
        Méthode pour valider le coup en fonction des cartes sélectionnées et du coup précédent.
        Retourne True si le coup est valide, False sinon.
        """

        if len(selected_cards) != len(previous_coup):
            return False

        premierCard = selected_cards[0].val
        if any(card.val != premierCard for card in selected_cards):
            return False

        for i in range(len(selected_cards)):
            if selected_cards[i].puissance <= previous_coup[i].puissance:
                return False


        for i in range(len(selected_cards)):
            if selected_cards[i].puissance <= previous_coup[i].puissance:
                return False

        return True


    def saisir_coup(self, previous_coup=None):
        """
        Méthode pour saisir un coup.
        Demande à l'utilisateur de choisir des cartes et valide le coup.
        Retourne le coup si valide, None sinon.
        """

        tabCoup = []

        print("Numéro du tour ",self.jeu.nb_tour)

        # Si le dernier joueur a jouer un 2, passer le tour tout les joueurs
        if previous_coup and previous_coup[0].puissance == 15 and self.jeu.dernierAvoirJouer != self.joueur and self.jeu.dernierAvoirJouer not in self.jeu.tabWin:
            print("\nVous avez passer votre tour car un 2 a été joué.\n")
            self.jeu.passage_succesif += 1
            return previous_coup

        if len(self.jeu.joueurs) - len(self.jeu.tabWin) == self.jeu.passage_succesif:
            print("\nVous controller le jeu !\nTous les autres joueurs ont passé leur tour.\n")
            previous_coup = None
            self.jeu.nb_carte_autorise = None
            self.nb_carte_autorise = None

        elif self.jeu.dernierAvoirJouer == self.joueur:
            print("\nVous controller le jeu !\nVous etes le dernier joueur a avoir jouer.\n")
            previous_coup = None
            self.jeu.nb_carte_autorise = None
            self.nb_carte_autorise = None

        if previous_coup is not None:
            print("\nCartes sur la tables :")
            for carte in previous_coup:
                print("-", carte)

            print("\nPuissance des carte sur le jeu en cours:", previous_coup[0].puissance)

        while True:

            if self.nb_carte_autorise is not None:
                print(f"\nVous devez jouer {self.nb_carte_autorise} cartes.")

            choix = input(
                "\nChoisissez 1, 2, ou 3 de vos cartes par rapport aux POSITIONS DES CARTES (séparées par des ',' (Exemple 1,2,3))\n"
                "Ou tapez 'p' pour passer votre tour, ou 'q' pour quitter le jeu: \n")

            if choix.lower() == 'p':
                self.jeu.passage_succesif += 1
            else:
                self.jeu.passage_succesif = 0

            if choix.lower() == 'q':
                print(f"\nJeu interrompu par {self.joueur.nom}. À bientôt !\n")
                exit(0)
            elif choix.lower() == 'p':

                if self.jeu.nb_tour == 1 and self.joueur == self.jeu.joueurs[0]:
                    print("\nVous ne pouvez pas passer votre tour car vous etes le 1er joueur du jeu, vous devez jouer.\n")
                    continue

                if self.jeu.dernierAvoirJouer == self.joueur:
                    print("\nVous ne pouvez pas passer votre tour, car vous etes le derniers joueur a avoir jouer, vous devez jouer (Vous controller le jeu !).\n")
                    continue
                else:
                    print("\nVous avez choisi de passer votre tour.\n")
                    return previous_coup


            else:
                coupJouer = choix.split(',')
                try:
                    positions = [int(pos.strip()) for pos in coupJouer]
                except ValueError:
                    print("\nErreur : Veuillez entrer des nombres entiers uniquement séparer par des virgules. Veuillez réessayer.\n")
                    continue

                if not self.check_doublon(coupJouer):
                    print("\nVous ne pouvez pas choisir deux fois la même carte. Veuillez réessayer.\n")
                    continue



                if len(positions) < 1 or len(positions) > 3:
                    print("\nVous devez choisir entre 1 et 3 cartes. Veuillez réessayer.\n")
                    continue

                if self.nb_carte_autorise is not None and len(positions) != self.nb_carte_autorise:
                    print(f"\nVous devez jouer {self.nb_carte_autorise} cartes. Veuillez réessayer.\n")
                    continue

                # Vérifcation si les Position sont presente dans la main du joueur
                selected_cards = []
                for pos in positions:
                    for carte in self.joueur.main:
                        if carte.position == pos:
                            selected_cards.append(carte)
                            break

                if len(selected_cards) != len(positions):
                    print("\nVeuillez choisir des positions valides dans votre main.\n")
                    continue

                # Vérifcation si les cartes jouer ont la meme puissance
                premier_Carte = selected_cards[0].puissance
                bool_verif = True
                for card in selected_cards[1:]:
                    if card.puissance != premier_Carte:
                        bool_verif = False
                        break

                if bool_verif is False:
                    print(
                        "\nToutes les cartes que vous jouez doivent avoir la même valeur (puissance). Veuillez réessayer.\n")
                    continue

                if previous_coup is not None:
                    if not self.validate_coup(selected_cards, previous_coup):
                        print("\nLe coup que vous avez choisi n'est pas valide. Veuillez réessayer.\n")
                        continue

                tabCoup = selected_cards


                if tabCoup[0].puissance == 15:
                    self.jeu.passage_succesif = 0

                for carte in tabCoup:
                    self.joueur.main.remove(carte)
                break

        return tabCoup












