class voiture:
    def __init__(self, marque, modele, couleur, prix_couleur, prix_modele):
        self.marque = marque
        self.modele = modele
        self.prix_modele = prix_modele
        self.couleur = couleur
        self.prix_couleur = prix_couleur
        self.prix_voitur = self.prix_voiture()

    def prix_voiture(self):
        return self.prix_modele*self.prix_couleur


if __name__ == "__main__":
    v = voiture("BMW", "Panda", "rouge", 2.5, 2000)


print(v.__dict__)
