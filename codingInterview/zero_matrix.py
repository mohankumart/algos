#zero matrix problem
from sys import stdout


def zero_matrix(my_array, matrix):
    for i in range(matrix):
        for j in range(matrix):
            #import pdb;pdb.set_trace()
            if my_array[i][j] == 0:
                #import pdb;pdb.set_trace()
                #change the row to zero
                    #keep the row contsant and change the column from 0 to n-1
                for m in range(matrix):
                    my_array[i][m] = 0
                for n in range(matrix):
                    my_array[n][j] = 0
                #printMatrix(my_array, matrix) 
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


