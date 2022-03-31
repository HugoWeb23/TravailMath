import numpy as np

"""
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

def polySorting(elem):
    return elem[1]

def displayResult(result):
    # L'opérateur ternaire permet d'afficher un + devant le monôme s'il ne se situe pas en première position ET si son résulat est > 0
    string = ""
    count = 0
    for mon in result:
        if mon[1] == 1:
            if mon[0] > 1 or mon[0] < -1:
                string += ("+" if count > 0 and mon[0] > 0 else "")+str(mon[0]) + base + " "
            elif mon[0] == 1 or mon[0] == -1:
                string += ("+" if count > 0 and mon[0] > 0 else "")+base + " "
        elif mon[1] == 0:
            string += ("+" if count > 0 and mon[0] > 0 else "")+str(mon[0]) + " "
        else:
            if mon[0] > 1 or mon[0] < -1:
                string += ("+" if count > 0 and mon[0] > 0 else "")+str(mon[0]) + base + "^" + str(mon[1])+" "
            elif mon[0] == 1 or mon[0] == -1:
                string += ("+" if count > 0 and mon[0] > 0 else "")+base + "^" + str(mon[1]) + " " # Si le coefficient est égal à 1 je le supprime, ce qui donne (ex: 1x^5 => x^5)
        count += 1
    return string

def findIndexPolyByExp(array, exposant): # L'index est-il présent dans le tableau de polynômes ? (Si oui, retourne l'index, sinon retourne -1)
    index = -1
    for poly in range(len(array)):
        if array[poly][1] == exposant:
            return poly
    return index

def multipliPoly(poly1, poly2):
    result = []
    for polyOneIndex in range(len(poly1)):
        for polyTwoIndex in range(len(poly2)):
            result.append([poly1[polyOneIndex][0] * poly2[polyTwoIndex][0], poly1[polyOneIndex][1] + poly2[polyTwoIndex][1]])

    sumpoly1 = []
    for p in result:  # Additionne les termes semblables
        index = findIndexPolyByExp(sumpoly1, p[1])
        if index != -1:
            sumpoly1[index][0] = sumpoly1[index][0] + p[0]
        else:
            sumpoly1.append(p)
    result = sumpoly1
    result.sort(key=polySorting, reverse=True) # Ordonne le résultat
    return displayResult(result)


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


print(f"Résultat (produit de deux polynômes) : {multipliPoly(poly1, poly2)}")