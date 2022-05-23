import numpy as np

base = input("Veuillez saisir la base du polynôme : ").lower()
coefficient = int(input("Veuillez saisir le coefficient : "))
nb_mon = int(input("Veuillez saisir le nombre de monômes dans le polynôme : "))
poly = []

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

def multipliPolyByCoef(poly):
    for p in range(len(poly)):
        poly[p][0] = poly[p][0] * coefficient
    poly.sort(key=polySorting, reverse=True)  # Ordonne le résultat
    return displayResult(poly)

for monome in range(nb_mon):
    saisie = input(f"Veuillez saisir le monôme {monome + 1} du polynôme : ")
    split = saisie.split('^')
    if len(split) > 1: # La chaîne contient le caractère ^ (ex: 5^3) ?
        split = [split[0].replace(base, '')] + split[1:] # J'enlève la base (si elle n'est pas présente rien ne change)
    if len(split) == 1: # La chaîne ne contient pas le caractère ^ (ex: 5x ou 5)
        if (base in split[0]) == False: # La base est-elle absente dans la chaîne (ex: 5) ?
            split.append(0) # Je garde le nombre tel quel et j'ajoute 0 dans le tableau pour indiquer qu'il s'agit d'un nombre sans base
        elif (base in split[0]) == True: # La base est-elle présente dans la chaîne (ex: 5x) ?
            split = [split[0].replace(base, ''), 1] # J'enlève la base et j'ajoute 1 dans le tableau pour indiquer qu'il s'agit d'un nombre avec la base
    split = np.asarray(split, dtype=np.int32, order='C')
    poly.append(split)

print(f"Résultat (produit d'un polynôme par un coefficient réel) : {multipliPolyByCoef(poly)}")