import numpy as np

nc_mat1 = int(input("Entrez le nombre de colonnes de la matrice 1 : "))
nl_mat1 = int(input("Entrez le nombre de lignes de la matrice 1 : "))
nc_mat2 = int(input("Entrez le nombre de colonnes de la matrice 2 : "))
nl_mat2 = int(input("Entrez le nombre de lignes de la matrice 2 : "))

if nc_mat1 != nl_mat2:
    print("Incompatibilité des matrices !")
    quit()

mat1 = [[0 for i in range(0,nc_mat1)] for j in range(0,nl_mat1)]
mat2 = [[0 for i in range(0,nc_mat2)] for j in range(0,nl_mat2)]

for matrice in range(2):
    for ligne in range(eval('nl_mat%d'% (matrice+1))):
        saisie=input(f'Veuillez saisir la ligne {ligne + 1} de la matrice {matrice + 1} ({eval("nc_mat%d"% (matrice+1))} chiffres), séparez les chiffres par une virgule : ').split(",")
        while (len(saisie) != eval("nc_mat%d"% (matrice+1))):
            print(f"Le nombre de chiffres doit être égal au nombre de colonnes ({eval('nc_mat%d'% (matrice+1))} colonnes)")
            saisie = input(
                f'Veuillez saisir la ligne {ligne + 1} de la matrice {matrice + 1} ({eval("nc_mat%d"% (matrice+1))} chiffres), séparez les chiffres par une virgule : ').split(
                ",")
        if matrice == 0:
            mat1[ligne] = np.asarray(saisie, dtype=np.float64, order='C')
        elif matrice == 1:
            mat2[ligne] = np.asarray(saisie, dtype=np.float64, order='C')

result = [[0 for i in range(0,nc_mat2)] for j in range(0,nl_mat1)]

for colonne in range(nc_mat2):
    for ligne in range(nl_mat1):
        somme = 0
        for sous_ligne in range(nc_mat1):
            somme += mat1[ligne][sous_ligne] * mat2[sous_ligne][colonne]
        result[ligne][colonne] = somme

print(f"Résultat (multiplication de deux matrices) :  {result}")