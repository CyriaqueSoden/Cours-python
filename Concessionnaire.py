from Class_consession import *
from Class_client import client
import random
liste_voiture =[]

v = voiture()
h = client("pithon", "mathieu")
w = 0

while h.budget < v.prix_voiture :
    w += 1
    v = voiture()
    liste_voiture.append(v)
    if w == 5 :
        print("pas de voiture dans le budget")
        break
    
    



print(v.__dict__)
print(h.__dict__)
