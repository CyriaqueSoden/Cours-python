import random


class client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.budget = self.budge()

    def budge(self):
        return random.randint(500, 502)
