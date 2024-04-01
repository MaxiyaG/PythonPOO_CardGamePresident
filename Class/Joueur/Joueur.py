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

    def passer(self):
        pass


    def __repr__(self):
        return f"Joueur {self.nom} : {self.main}"

