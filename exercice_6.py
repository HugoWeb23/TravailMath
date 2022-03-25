import re
import numpy as np

eq1 = input("Saisissez l'équation 1 (exemple: -2, 12 = 2) ")
eq2 = input("Saisissez l'équation 2 (exemple: -2, 12 = 2) ")

eq1array = re.split(',|=', eq1)
eq1 = np.asarray(eq1array, dtype=np.float64, order='C')

eq2array = re.split(',|=', eq2)
eq2 = np.asarray(eq2array, dtype=np.float64, order='C')

mat = []
mat.append(eq1)
mat.append(eq2)
D = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
DX = mat[0][2] * mat[1][1] - mat[0][1] * mat[1][2]
DY = mat[0][0] * mat[1][2] - mat[0][2] * mat[1][0]

x = DX / D
y = DY / D

print(f'X = {round(x, 2)}, Y = {round(y, 2)}')