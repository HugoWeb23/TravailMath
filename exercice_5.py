import matplotlib.pyplot as plot
from matplotlib_venn import venn3, venn3_unweighted
from random import *
from functools import reduce

def GenererNombres(limite, debut, fin):
    nombres = []
    while len(nombres) != limite:
        random = randint(debut, fin)
        if not (random in nombres):
            nombres.append(random)
    return nombres

nombres = GenererNombres(25, 1, 200)
multiples = GenererNombres(3, 2, 9)

A = []
B = []
AB = []
C = []
AC = []
BC = []
ABC = []
Dehors = []

for nombre in nombres:
    modulo = []
    for nb in range(3):
        modulo.append(nombre % multiples[nb])
    if modulo[0] == 0:
        modulo[0] = 1
    else:
        modulo[0] = 0
    if modulo[1] == 0:
        modulo[1] = 2
    else:
        modulo[1] = 0
    if modulo[2] == 0:
        modulo[2] = 4
    else:
        modulo[2] = 0

    sum = reduce(lambda x, y: x + y, modulo)

    if sum == 0:
        Dehors.append(nombre)

    if sum == 1:
        A.append(nombre)
    if sum == 2:
        B.append(nombre)
    if sum == 4:
        C.append(nombre)
    if sum == 3:
        AB.append(nombre)
    if sum == 5:
        AC.append(nombre)
    if sum == 6:
        BC.append(nombre)
    if sum == 7:
        ABC.append(nombre)

A = "\n".join(map(str, A))
B = "\n".join(map(str, B))
AB = "\n".join(map(str, AB))
C = "\n".join(map(str, C))
AC = "\n".join(map(str, AC))
BC = "\n".join(map(str, BC))
ABC = "\n".join(map(str, ABC))
Dehors = ", ".join(map(str, Dehors))

items=[A, B, AB, C, AC, BC, ABC]
labels=[]

for a in range(3):
    label = f"Divisible par {multiples[a]}"
    labels.append(label)

venn3_unweighted(subsets=items,set_labels=labels,alpha=0.6)
plot.title(Dehors)
plot.show()