from Class_voiture import voiture
from Class_client import client

compteur_de_boucle = 0
voiture_du_client = ""
liste_client = {}


while True :
    vroum = voiture()
    nom = input("nom  :")
    if nom in liste_client:
        pass
    else:
        liste_client = {nom: client(nom)}


    while liste_client[nom].budget < vroum.prix_voiture:
        compteur_de_boucle += 1
        vroum = voiture()
        liste_client[nom].voiture.append(vroum)
        if compteur_de_boucle == 5:
            print("pas de voiture dans le budget")
            break

    liste_client[nom].achat_voiture(vroum)


    print("budget :",liste_client[nom].budget)
    for i in liste_client[nom].voiture :
        print(i.__dict__)