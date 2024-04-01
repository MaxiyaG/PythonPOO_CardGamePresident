from Class.Jeu.Jeu import Jeu

if __name__ == "__main__":

    nb_Joueur = Jeu.define_nb_Joueur(None)
    nb_Carte = Jeu.define_nb_Carte(None)

    jeu = Jeu(nb_Joueur, nb_Carte)
    jeu.initialisation()
    jeu.jeu()

