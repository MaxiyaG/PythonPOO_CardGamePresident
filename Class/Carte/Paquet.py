from Class.Carte.Carte import Carte
import random 

class Paquet(Carte):

    # Constructor
    def __init__(self):

        self.listCard = []

        for symbol in Carte.symbolValide:
            for val in Carte.valeurValide:

                puissance = Carte.attribut_puissance(val)

                c = Carte(val, symbol, puissance, position=None)
                Carte.__repr__(c)
                self.listCard.append(c)

    def __repr__(self):
        return str(self.listCard)

    # Méthode : mélanger Paquet
    def melanger(self):
        random.shuffle(self.listCard)

    # Méthode : coupé Paquet
    def couper(self):
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

  #  def couper(self):
 #     nb_carte = random.randint(0,len(self.listCard))
  #    self.listCard = self.listCard[nb_carte:] + self.listCard[:nb_carte]

    # Méthode : pioché la carte en haut de la pile
    def pioche(self):
        carte_pioche = self.listCard[0]
        self.listCard.pop(0)
        return carte_pioche

    # Méthode : distribuer les cartes au joueur
    def distribuer(self, nb_Joueur, nb_Carte):
        distribution = [[] for i in range(0, nb_Joueur)]

        for i in range(0, nb_Carte):
            for j in range(0, nb_Joueur):
                carte = self.pioche()
                carte.position = i + 1
                distribution[j].append(carte)

        return distribution
