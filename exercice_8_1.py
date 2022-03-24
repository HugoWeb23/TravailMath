import numpy as np

nc=int(input("Entrer le nombre de colonne(s) des matrices : "))

while(nc < 1 or nc > 4):
    print("Vous devez saisir un chiffre entre 1 et 4")
    nc = int(input("Entrer le nombre de colonne(s) des matrices : "))

nl=int(input("Entrer le nombre de ligne(s) des matrices : "))

while(nl < 1 or nl > 4):
    print("Vous devez saisir un chiffre entre 1 et 4")
    nl=int(input("Entrer le nombre de ligne(s) des matrices : "))

mat = [[0 for i in range(0,nc)] for j in range(0,nl)]
mat2 = [[0 for i in range(0,nc)] for j in range(0,nl)]

for matrice in range(2):
    for ligne in range(nl):
        saisie=input(f'Veuillez saisir la ligne {ligne + 1} de la matrice {matrice + 1} ({nc} chiffres), séparez les chiffres par une virgule : ').split(",")
        while(len(saisie) != nc):
            print(f"Le nombre de chiffres doit être égal au nombre de colonnes ({nc} colonnes)")
            saisie = input(f'Veuillez saisir la ligne {ligne + 1} de la matrice {matrice + 1} ({nc} chiffres), séparez les chiffres par une virgule : ').split(",")
        if matrice == 0:
            mat[ligne] = np.asarray(saisie, dtype=np.float64, order='C')
        elif matrice == 1:
            mat2[ligne] = np.asarray(saisie, dtype=np.float64, order='C')

result = [[0 for i in range(0,nc)] for j in range(0,nl)]

for ligne in range(nl):
    for colonne in range(nc):
        result[ligne][colonne] = mat[ligne][colonne] + mat2[ligne][colonne]

print(f"Résultat (addition de deux matrices) : {result}")
