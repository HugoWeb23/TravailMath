import math

a = float(input('Veuillez saisir la valeur de A : '))
b = float(input('Veuillez saisir la valeur de B : '))
c = float(input('Veuillez saisir la valeur de C: '))

delta = b ** 2 - 4 * a * c

if delta < 0 :
    print("Il n'y a pas de solution !")
elif delta == 0 :
    x = (-b) / (2 * a)
    print("Solution : ", x)
else :
    x1 = (-b-math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print("Les solutions sont : ", format(x1, ".2f"), " et ", format(x2, ".2f"))
