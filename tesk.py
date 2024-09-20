import numpy as np
import math

image_matrix = np.array([
        [100, 150, 200, 250],
        [50, 75, 125, 175],
        [0, 25, 50, 100],
        [255, 128, 64, 32]
    ]
)

def transpose(m):
    dimensions = m.shape
    rows, columns = dimensions
    temp = np.zeros((columns, rows))
    for i in range(0,columns):
        for j in range(0,rows):
            temp[i][j] = m[j][i]
    return temp

def pivoter_pour_90(m):
    matrice_transpose = transpose(m)
    rotated_matrix = pivoter_horizentalement(matrice_transpose)
    return rotated_matrix
        

def pivoter_verticalement(m):
    dimensions = m.shape
    rows, columns = dimensions
    matrice_temp = np.zeros((rows,columns))
    row = rows
    for i in range(0,rows) : 
        row = row - 1
        for j in range(0,columns):
            matrice_temp[row][j] = m[i][j]
    return matrice_temp


def pivoter_horizentalement(m):
    dimensions = m.shape
    rows, columns = dimensions
    matrice_temp = np.zeros((rows, columns))
    for i in range(0,rows):
        column = columns
        for j in range(0,columns):
            column = column - 1
            matrice_temp[i][column] = m[i][j]
    return matrice_temp

def transformer_whiteblack(m,treshold):
    dimensions = m.shape
    rows, columns = dimensions
    matrice_temp = np.zeros((rows, columns))
    for i in range(0,rows):
        for j in range(0,columns):
            if(m[i][j] > treshold):
                matrice_temp[i][j] = 255
            else:
                matrice_temp[i][j] = 0
    print("with threshold",treshold)
    return matrice_temp

def blur_image(m):
    dimensions = m.shape
    rows, columns = dimensions
    matrice_temp = np.zeros((rows, columns))
    num = rows * columns
    for i in range(0,rows):
        for j in range(0,columns):
            matrice_temp[i][j] = math.floor(m[i][j] / num)
    return matrice_temp


result = pivoter_pour_90(image_matrix)

check = True
while(check):
    print("1 . pivoter 90 degree le matrice")
    print("2 . pivoter horizentalment")
    print("3 . pivoter verticalement")
    print("4 . blur the picture")
    print("5 . make the picture black and white")
    choice = int(input("enter the choice : "))
    if(choice > 5 or choice < 0):
        print("error no operation match")
    else:
        check = False

if(choice == 1):
    result = pivoter_pour_90(image_matrix)
elif(choice == 2): 
    result = pivoter_horizentalement(image_matrix)
elif(choice == 3):
    result = pivoter_verticalement(image_matrix)
elif(choice == 4):
    result = blur_image(image_matrix)
elif(choice == 5):
    treshold = int(input("enter the treshold :"))
    result = transformer_whiteblack(image_matrix,treshold)

print(result)
