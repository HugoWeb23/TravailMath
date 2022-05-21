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
if nb_mon1 != nb_mon2:
    print("Les polynômes doivent avoir la même taille")
    quit()
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
    # L'opérateur ternaire permet d'afficher un + devant le monôme s'il ne se situe pas en première position ET si son résulat est > 0
    string = ""
    count = 0
    for mon in result:
        if mon[1] == 1: # Si l'exposant est 1 (ex: 5x)
            if mon[0] > 1 or mon[0] < -1: # Si le coefficient est supérieur à 1 ou inférieur à -1
                string += ("+" if count > 0 and mon[0] > 0 else "")+str(mon[0]) + base + " " # On affiche le coefficient et la base (ex: 6x)
            elif mon[0] == 1 or mon[0] == -1: # Si le coefficient est égal à 1 ou à -1
                string += ("+" if count > 0 and mon[0] > 0 else "-")+base + " " # On affiche seulement la base
        elif mon[1] == 0: # Si l'exposant est 0 (nombre sans base)
            string += ("+" if count > 0 and mon[0] > 0 else "")+str(mon[0]) + " " # On affiche seulement le nombre
        else:
            if mon[0] > 1 or mon[0] < -1:
                string += ("+" if count > 0 and mon[0] > 0 else "")+str(mon[0]) + base + "^" + str(mon[1])+" " # Ex: 5x^5
            elif mon[0] == 1 or mon[0] == -1:
                string += ("+" if count > 0 and mon[0] > 0 else "-")+base + "^" + str(mon[1]) + " " # Si le coefficient est égal à 1 je le supprime, ce qui donne (ex: 1x^5 => x^5)
        count += 1
    return string

def addPoly(poly1, poly2):
    sumpoly1 = []
    for p in poly1: # Additionne les monômes de même exposant au sein du polynôme 1
        index = findIndexPolyByExp(sumpoly1, p[1])
        if index != -1:
            sumpoly1[index][0] = sumpoly1[index][0] + p[0]
        else:
            sumpoly1.append(p)
    result = sumpoly1

    for position in range(len(poly1)):
        index = findIndexPolyByExp(result, poly2[position][1])
        if index != -1:
            result[index][0] = result[index][0] + poly2[position][0]
        else:
            result.append(poly2[position])
    result.sort(key=polySorting, reverse=True)
    return displayResult(result)

print(addPoly(poly1, poly2))