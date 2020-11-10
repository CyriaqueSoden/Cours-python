from Class_voiture import Voiture
from Class_client import Client

compteur_boucle = 0
voiture_du_client = ""
liste_client = {}


while True :
    vroum = Voiture()
    nom = input("nom  :")
    if nom in liste_client:
        pass
    else:
        liste_client = {nom: Client(nom)}


    while liste_client[nom].budget < vroum.prix_voiture:
        compteur_boucle += 1
        vroum = Voiture()
        liste_client[nom].voiture.append(vroum)
        if compteur_boucle == 5:
            print("pas de voiture dans le budget")
            break

    liste_client[nom].achat_voiture(vroum)


    print("budget :",liste_client[nom].budget)
    for i in liste_client[nom].voiture :
        print(i.__dict__)
