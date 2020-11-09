import random


class voiture:
    def __init__(self, marque, modele, couleur, prix_couleur, prix_modele):
        self.marque = marque
        self.modele = modele
        self.prix_modele = prix_modele
        self.couleur = couleur
        self.prix_couleur = prix_couleur
        #self.prix_voitur = self.prix_voiture()


marque = [("Peugeot", 1), ("Renault", 1), ("Opel", 1), ("Citroën", 1.2),
          ("Volkswagen", 1.5), ("Mercedes", 2), ("BMW", 3), ("Fiat", 0.8)]


a = random.randint(0, len(marque))
b =
v = voiture(marque[a][0], "Panda", "rouge", 2.5, 2000)

modele = [i for i in range(10)]


# # marque, modele, couleur, prix_couleur, prix_modele


print(v.__dict__)
