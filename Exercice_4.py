import numpy as np

"""
Le programme gère actuellement les polynômes avec une seule base (ex: 5x^3, 5x) et les nombres normaux (ex: 4, 5, 6)
Représentation des monômes dans le programme :

2x3 = [2, 3]
2x = [2, 1]
2 = [2, 0]
"""

base = input("Veuillez saisir la base des polynômes : ").lower()
nb_mon1 = int(input("Veuillez saisir le nombre de monômes dans le polynôme 1 : "))
nb_mon2 = int(input("Veuillez saisir le nombre de monômes dans le polynôme 2 : "))
poly1 = []
poly2 = []

for polynome in range(2):
    for monome in range(eval('nb_mon%d'% (polynome+1))):
        saisie = input(f"Veuillez saisir le monôme {monome + 1} du polynôme {polynome + 1} : ")
        split = saisie.split('^')
        if len(split) > 1: # La chaîne contient le caractère ^ (ex: 5^3) ?
            split = [split[0].replace(base, '')] + split[1:] # J'enlève la base (si elle n'est pas présente rien ne change)
        if len(split) == 1: # La chaîne ne contient pas le caractère ^ (ex: 5x ou 5)
            if (base in split[0]) == False: # La base est-elle absente dans la chaîne (ex: 5) ?
                split.append(0) # Je garde le nombre tel quel et j'ajoute 0 dans le tableau pour indiquer qu'il s'agit d'un nombre sans base
            elif (base in split[0]) == True: # La base est-elle présente dans la chaîne (ex: 5x) ?
                split = [split[0].replace(base, ''), 1] # J'enlève la base et j'ajoute 1 dans le tableau pour indiquer qu'il s'agit d'un nombre avec la base
        split = np.asarray(split, dtype=np.int32, order='C')
        if polynome == 0:
            poly1.append(split)
        elif polynome == 1:
            poly2.append(split)

def findIndexPolyByExp(array, exposant): # L'index est-il présent dans le tableau de polynômes ? (Si oui, retourne l'index, sinon retourne -1)
    index = -1
    for poly in range(len(array)):
        if array[poly][1] == exposant:
            return poly
    return index

def polySorting(elem):
    return elem[1]

def displayResult(result):
    string = ""
    for mon in result:
        if mon[1] == 1:
            string += str(mon[0]) + base + " "
        elif mon[1] == 0:
            string += str(mon[0]) + " "
        else:
            string += str(mon[0]) + base + "^" + str(mon[1])+" "
    return string

def addPoly(poly1, poly2):
    result = poly1
    if len(poly1) != len(poly2):
        print("Les polynômes doivent avoir la même taille")
        quit()

    for position in range(len(poly1)):
        index = findIndexPolyByExp(result, poly2[position][1])
        if index != -1:
            result[index][0] = result[index][0] + poly2[position][0]
        else:
            result.append(poly2[position])
    result.sort(key=polySorting, reverse=True)
    return displayResult(result)

print(addPoly(poly1, poly2))