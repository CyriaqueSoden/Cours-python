import random


class client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.budget = random.randint(300, 5000)

