from sys import stdout


def rotateMatrix(my_array, matrix):
    temp1 = my_array[0][0]
    temp2 = my_array[0][0]
    loopLength = matrix
    left = 0
    right = 0
    for loop in range(4):
        if loop == 0:
            while right < loopLength-1:
                temp1 = temp2
                temp2 = my_array[left][right+1]
                my_array[left][right+1] = temp1
                right += 1
        elif loop == 1:
            while left < loopLength-1:
               temp1 = temp2
               temp2 = my_array[left+1][right]
               my_array[left+1][right] = temp1
               left += 1
        elif loop == 2:
            while right > 0:
               temp1 = temp2
               temp2 = my_array[left][right-1]
               my_array[left][right-1] = temp1
               right -= 1
        elif loop == 3:
            while left > 0:
              temp1 = temp2
              temp2 = my_array[left-1][right]
              my_array[left-1][right] = temp1
              left -= 1
    printMatrix(my_array, matrix)

def createMatrix():
    matrix = int(raw_input('Enter The Matrix: '))
    my_array = [[0 for j in range(matrix)] for i in range(matrix)]
    for i in range(matrix):
        for j in range(matrix):
            my_input = raw_input(("Enter ({},{})").format(i,j) + ': ')
            my_array[i][j] = my_input 
    print("Input\n")
    printMatrix(my_array, matrix)
    rotateMatrix(my_array, matrix)

def printMatrix(my_array, matrix):
    for i in range(matrix):
        for j in range(matrix):
            stdout.write(str(my_array[i][j]) + '   ')
        print('\n') 

createMatrix()

