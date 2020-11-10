from Class_consession import *
from Class_client import client
import random
liste_voiture =[]

v = voiture()
h = client("pithon", "mathieu")


if h.budget < v.prix_voiture :
    liste_voiture.append(voiture())
    print(liste_voiture)





print(v.__dict__)
print(h.__dict__)
