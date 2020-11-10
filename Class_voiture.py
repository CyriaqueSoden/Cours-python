"""
Class_voiture
"""
import random


class Voiture:
    """
    Init
    """

    def __init__(self):
        self.marque = [("Peugeot", 1), ("Renault", 1), ("Opel", 1), ("Citroën", 1.2),
                       ("Volkswagen", 1.5), ("Mercedes", 2), ("BMW", 3), ("Fiat", 0.8)]
        self.modele = [100, 200, 300, 400, 500]
        self.couleur = [("noir", 1), ("rouge", 1), ("blanc", 1), ("gris", 1.2),
                        ("carbon", 1.5), ("orange", 2), ("jaune", 3), ("vert", 0.8)]
        self.Randv1()
        self.Randv2()

    def Randv1(self):
        self.randmarque = random.randint(0, len(self.marque)-1)
        self.randmodele = random.randint(0, len(self.modele)-1)
        self.randcouleur = random.randint(0, len(self.couleur)-1)

    def Randv2(self):
        self.numéro_de_serie = random.randint(0, 1000000000)
        self.marque = self.marque[self.randmarque][0]
        self.modele = self.modele[self.randmodele]
        self.couleur = self.couleur[self.randcouleur][0]
        self.prix_voiture = self.marque[self.randmarque][1] * \
            self.modele[self.randmodele]*self.couleur[self.randcouleur][1]
