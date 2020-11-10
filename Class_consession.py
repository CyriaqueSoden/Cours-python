import random


class voiture:
    def __init__(self):
        marque = [("Peugeot", 1), ("Renault", 1), ("Opel", 1), ("Citroën", 1.2),
                   ("Volkswagen", 1.5), ("Mercedes", 2), ("BMW", 3), ("Fiat", 0.8)]
        modele = [100, 200, 300, 400, 500]
        couleur = [("noir", 1), ("rouge", 1), ("blanc", 1), ("gris", 1.2),
                    ("carbon", 1.5), ("orange", 2), ("jaune", 3), ("vert", 0.8)]


        a = random.randint(0, len(marque)-1)
        b = random.randint(0, len(modele)-1)
        c = random.randint(0, len(couleur)-1)

        self.numéro_de_serie = random.randint(0,1000000000)
        self.marque = marque[a][0]
        self.modele = modele[b]
        self.couleur = couleur[c][0]
        self.prix_voiture = marque[a][1]*modele[b]*couleur[c][1]