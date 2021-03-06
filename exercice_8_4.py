import numpy as np

nc=int(input("Entrez le nombre de colonne(s) de la matrice: "))

while(nc < 1 or nc > 4):
    print("Vous devez saisir un chiffre entre 1 et 4")
    nc = int(input("Entrez le nombre de colonne(s) de la matrice : "))

nl = int(input("Entrez le nombre de ligne(s) de la matrice : "))

while (nl < 1 or nl > 4):
    print("Vous devez saisir un chiffre entre 1 et 4")
    nl = int(input("Entrez le nombre de ligne(s) de la matrice : "))

mat = [[0 for i in range(0,nc)] for j in range(0,nl)]

for ligne in range(nl):
    saisie = input(f'Veuillez saisir la ligne {ligne + 1} ({nc} chiffres), séparez les chiffres par une virgule : ').split(",")
    while (len(saisie) != nc):
        print(f"Le nombre de chiffres doit être égal au nombre de colonnes ({nc} colonnes)")
        saisie = input(f'Veuillez saisir la ligne ({nc} chiffres), séparez les chiffres par une virgule : ').split(",")
    mat[ligne] = np.asarray(saisie, dtype=np.float64, order='C')


int = nc
nc = nl
nl = int

result = [[0 for i in range(0,nc)] for j in range(0,nl)]

for ligne in range(nl):
    for colonne in range(nc):
        result[ligne][colonne] = mat[colonne][ligne]

print("Résultat (matrice transposée) :\n")
for i in range(len(result)):
    print(result[i])