from sys import stdout


def rotateMatrix(my_array, matrix):
    loopend = matrix-1
    loopstart = 0
    looplength = matrix - 1
    left = 0
    right = 0
    while looplength >= 1:
        print loopend
        import pdb;pdb.set_trace()
        for mainloop in range(looplength):
            temp1 = my_array[loopstart][loopstart]
            temp2 = my_array[loopstart][loopstart]
            for loop in range(4):
                if loop == 0:
                    while right < loopend:
                        temp1 = temp2
                        temp2 = my_array[left][right+1]
                        my_array[left][right+1] = temp1
                        right += 1
                elif loop == 1:
                    while left < loopend:
                        temp1 = temp2
                        temp2 = my_array[left+1][right]
                        my_array[left+1][right] = temp1
                        left += 1
                elif loop == 2:
                    while right > loopstart:
                        temp1 = temp2
                        temp2 = my_array[left][right-1]
                        my_array[left][right-1] = temp1
                        right -= 1
                elif loop == 3:
                    while left > loopstart:
                        temp1 = temp2
                        temp2 = my_array[left-1][right]
                        my_array[left-1][right] = temp1
                        left -= 1
        loopend -= 1
        loopstart += 1
        looplength -= 2
        left = loopstart
        right = loopstart
    print("Output\n")
    printMatrix(my_array, matrix)

def createMatrix():
    matrix = int(raw_input('Enter The Matrix: '))
    my_array = [[0 for j in range(matrix)] for i in range(matrix)]
    n = 1
    for i in range(matrix):
        for j in range(matrix):
            #my_input = raw_input(("Enter ({},{})").format(i,j) + ': ')
            my_array[i][j] = n
            n += 1 
    print("Input\n")
    printMatrix(my_array, matrix)
    rotateMatrix(my_array, matrix)

def printMatrix(my_array, matrix):
    for i in range(matrix):
        for j in range(matrix):
            stdout.write(str(my_array[i][j]) + '    ')
        print('\n') 

createMatrix()

