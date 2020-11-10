from Class_voiture import voiture
from Class_client import client

liste_voiture =[]

vroum = voiture()
Cyriaque = client("Cyriaque", "Soden")
compteur_de_boucle = 0

while Cyriaque.budget < vroum.prix_voiture :
    compteur_de_boucle += 1
    vroum = voiture()
    if compteur_de_boucle == 5 :
        print("pas de voiture dans le budget")
        break
    
    



print(vroum.__dict__)
print(Cyriaque.__dict__)
