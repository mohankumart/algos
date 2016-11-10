#zero matrix problem
from sys import stdout


def zero_matrix(my_array, matrix):
    xMatrix = [1 for i in range(matrix)]
    yMatrix = [1 for j in range(matrix)]
    print xMatrix
    print yMatrix

    for i in range(matrix):
        for j in range(matrix):
            if my_array[i][j] == 0:
                xMatrix[i] = 0
                yMatrix[j] = 0

    for m in range(len(xMatrix)):
        if xMatrix[m] == 0:
            for n in range(matrix):
                my_array[m][n] = 0

    for m in range(len(yMatrix)):
        if yMatrix[m] == 0:
            for n in range(matrix):
                my_array[n][m] = 0
 
    printMatrix(my_array, matrix)


def createMatrix():
    matrix = int(raw_input('Enter The Matrix: '))
    my_array = [[0 for j in range(matrix)] for i in range(matrix)]
    print my_array
    for i in range(matrix):
        for j in range(matrix):
            my_input = raw_input(("Enter ({},{})").format(i,j) + ': ')
            my_array[i][j] = int(my_input)
    print("Input\n")
    printMatrix(my_array, matrix)
    zero_matrix(my_array, matrix)

def printMatrix(my_array, matrix):
    for i in range(matrix):
        for j in range(matrix):
            stdout.write(str(my_array[i][j]) + '    ')
        print('\n') 

createMatrix()


