class Joueur:


    def __init__(self, numero,nom, main):
        self.numero = numero
        self.nom = nom
        self.main = []

    def nb_Carte_En_Main(self):
        return len(self.main)

    def verif_victoir(self):
        if self.nb_Carte_En_Main() == 0:
            return True

        return False

    nb_carte_autorise = None

    def check_doublon(self, tabCoup):
        return len(tabCoup) == len(set(tabCoup))


    def saisir_coup(self):
        while True:
            choix = input(
                "Choisissez une, 2, ou 3 de vos cartes avec un chiffre séparer par des ',', ou faite pass avec 'p', ou 'q' pour quitter")
            if choix.lower() == 'q':
                print(f"Jeu interrompu par {self.nom}.")
                exit(0)
            elif choix.lower() == 'p':
                if Joueur.nb_carte_autorise is None:
                    print("Vous ne pouvez pas passer votre tour, vous devez jouer.\n")
                    continue
                else:
                    print("Vous avez choisi de passer votre tour.\n")
                    return
            else:
                tabCoup = choix.split(',')

                if self.check_doublon(tabCoup) == False:
                    print("Vous ne pouvez pas choisir deux fois la même carte.")
                    continue

                if len(tabCoup) < 1 or len(tabCoup) > 3:
                    print("Vous devez choisir entre 1 et 3 cartes.")
                    continue

                if Joueur.nb_carte_autorise is not None and len(tabCoup) != Joueur.nb_carte_autorise and len(
                        tabCoup) != len(self.main):
                    print(f"Vous devez jouer {Joueur.nb_carte_autorise} cartes.")
                elif all(1 <= int(coup) <= len(self.main) for coup in tabCoup):
                    if Joueur.nb_carte_autorise is None:
                        Joueur.nb_carte_autorise = len(tabCoup)
                    print("Cartes choisies: ", ', '.join(tabCoup))
                    break
                else:
                    print(f"Veuillez entrer des nombres entre 1 et {len(self.main)} séparés par des ','")
        return tabCoup








    def __repr__(self):
        return f"Joueur {self.nom} : {self.main}"

