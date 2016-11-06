#string compression

#using previous character
def compressString(str1):
    count = 0
    tempString = ''
    prevChar = ''
    for i in range(len(str1)):
        if i == 0:
            count += 1
            prevChar = str1[i]
            tempString += str1[i]
            if i == len(str1) - 1:
                tempString += str(count)
        else:
            if prevChar == str1[i]:
                count += 1
                if i == len(str1)-1:
                    tempString += str(count)
            else:
                tempString += str(count)
                count = 1
                prevChar = str1[i]
                tempString += str1[i]
                if i == len(str1) - 1:
                    tempString += str(count)


    return tempString

#str1 = raw_input("Enter String: ")

#print(compressString(str1))

