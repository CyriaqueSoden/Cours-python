from Class_voiture import voiture
from Class_client import client

liste_voiture =[]

vroum = voiture()
mathieu = client("pithon", "mathieu")
compteur_de_boucle = 0

while mathieu.budget < vroum.prix_voiture :
    compteur_de_boucle += 1
    vroum = voiture()
    liste_voiture.append(vroum)
    if compteur_de_boucle == 5 :
        print("pas de voiture dans le budget")
        break
    
    



print(vroum.__dict__)
print(mathieu.__dict__)
