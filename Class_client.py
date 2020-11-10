import random



class client:
    def __init__(self, nom):
        self.nom = nom
        self.budget = random.randint(300, 5000)
        self.voiture = []
    
    def achat_voiture(self,voiture_du_client):
        self.voiture.append(voiture_du_client)
