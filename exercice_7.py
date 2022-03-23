import re
import numpy as np

eq1 = input("Saisissez l'équation 1 (exemple: -2, 12, 45 = 2) ")
eq2 = input("Saisissez l'équation 2 (exemple: -2, 12, 45 = 2) ")
eq3 = input("Saisissez l'équation 3 (exemple: -2, 12, 45 = 2) ")

eq1array = re.split(', | = ', eq1)
eq1 = np.asarray(eq1array, dtype=np.float64, order='C')

eq2array = re.split(', | = ', eq2)
eq2 = np.asarray(eq2array, dtype=np.float64, order='C')

eq3array = re.split(', | = ', eq3)
eq3 = np.asarray(eq3array, dtype=np.float64, order='C')

mat = []
mat.append(eq1)
mat.append(eq2)
mat.append(eq3)

D = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) - mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) + mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])

if D == 0:
    print("Il n'y a aucune solution")
    quit()

DX = mat[0][3] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) - mat[0][1] * (mat[1][3] * mat[2][2] - mat[1][2] * mat[2][3]) + mat[0][2] * (mat[1][3] * mat[2][1] - mat[1][1] * mat[2][3])
DY = mat[0][0] * (mat[1][3] * mat[2][2] - mat[1][2] * mat[2][3]) - mat[0][3] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) + mat[0][2] * (mat[1][0] * mat[2][3] - mat[1][3] * mat[2][0])
DZ = mat[0][0] * (mat[1][1] * mat[2][3] - mat[1][3] * mat[2][1]) - mat[0][1] * (mat[1][0] * mat[2][3] - mat[1][3] * mat[2][0]) + mat[0][3] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])

x = DX / D
y = DY / D
z = DZ / D

print(f'X = {round(x, 2)}, Y = {round(y, 2)}, Z = {round(z, 2)}')