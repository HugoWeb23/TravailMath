poly1 = [[2, 4], [3,2], [4,3], [4, 1]]
poly2 = [[5,3], [6,4], [8, 1], [7,2]]

"""
2x3 = [2, 3]
2x = [2, 1]
2 = [2, 0]
"""

def findIndexPolyByExp(array, exposant):
    index = -1
    for poly in range(len(array)):
        if array[poly][1] == exposant:
            return poly
    return index

def polySorting(elem):
    return elem[1]


def addPoly(poly1, poly2):
    result = poly1
    if len(poly1) != len(poly2):
        print("Les polynômes doivent avoir la même taille")
        quit()

    for position in range(len(poly1)):
        index = findIndexPolyByExp(result, poly2[position][1])
        if index != -1:
            result[index][0] = result[index][0] + poly2[position][0]
        else:
            result.append(poly2[position])
    result.sort(key=polySorting, reverse=True)
    return result

print(addPoly(poly1, poly2))
