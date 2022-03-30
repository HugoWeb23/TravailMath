import numpy as np

def degre(mp):
    if type(mp[0]) == list:
        return mp[0][1]
    return mp[1]

def coef(mp):
    if type(mp[0]) == list :
        return mp[0][0]
    return mp[0]

def mono_plus_poly(c, e, p):
    for i in range(len(p)):  # on cherche le premier monôme de degré d ≤ e
        m = p[i]
        print(f"M = {m}")
        d = degre(m) # le degré du terme d'indice i de p
        print(f"D = {d}")
        if e == d: # trouvé !
            essai = c + coef(m) # attention !
            print(f"Essai (c + coef(m)) => {c} + {coef(m)} = {essai}")
            if essai == 0:
                print(f"Essai == 0 => {p[:i]} + {p[i+1:]}")
                return p[:i] + p[i+1:]
            print(f"p[:i] + [[essai,d]] + p[i+1:] => {p[:i]} + {[[essai,d]]}, {p[i+1:]}")
            return p[:i] + [[essai,d]] + p[i+1:]
        elif e > d: # insertion d'un nouvel élément !
            print(f"Insertion élément p[:i] + [[c,e]] + p[i:] : {p[:i] + [[c,e]] + p[i:]}")
            return p[:i] + [[c,e]] + p[i:]
    print(f"Return p + [[c,e]] : {p + [[c,e]]}")
    return p + [[c,e]]

def add(p1, p2):
    for m in p1:
        p2 = mono_plus_poly(coef(m), degre(m), p2)
    return p2

base = input("Veuillez saisir la base des polynômes : ")
nb_mon1 = int(input("Veuillez saisir le nombre de monômes dans le polynôme 1 : "))
nb_mon2 = int(input("Veuillez saisir le nombre de monômes dans le polynôme 2 : "))

poly1 = []
poly2 = []

def OrderPoly(elem):
    try:
        return elem[1]
    except IndexError:
        return 5555

for polynome in range(2):
    for monome in range(eval('nb_mon%d'% (polynome+1))):
        saisie = input(f"Veuillez saisir le monôme {monome + 1} du polynôme {polynome + 1} : ")
        split = saisie.split('^')
        split = np.asarray(split, dtype=np.float64, order='C')
        if polynome == 0:
            poly1.append(split)
        elif polynome == 1:
            poly2.append(split)

print(f"Résultat : {add(poly1, poly2)}")
