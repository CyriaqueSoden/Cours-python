"""
class client
"""
import random


class Client:
    """
    creation d'un client
    """

    def __init__(self, nom):
        self.nom = nom
        self.budget = self.budge()
        self.voiture = []

    def achat_voiture(self, voiture_du_client):
        self.voiture.append(voiture_du_client)

    def budge(self):
        return random.randint(300, 5000)
