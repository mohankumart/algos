str = raw_input("Enter the string: ")

def urlify(str):
    #count the spaces in the string
    spaceCount = 0
    for c in str:
        if c == " ":
            spaceCount += 1

    #replace the spaces in the string with %20 characters and reduce the count of the spaces
    resultlist = list()
    for c in str:
        if c != " ":
            resultlist.append(c)
        else:
            if spaceCount >= 3:
                resultlist.append('%')
                resultlist.append('2')
                resultlist.append('0')
                spaceCount -= 3
    return "".join(resultlist)

#print(urlify(str))

def urlify2(str):
    #import pdb;pdb.set_trace()
    resultString = ''
    first = False
    for c in reversed(str):
        if c != ' ':
            first = True

        if c == ' ' and first:
            resultString += '%02'
        elif first:
            resultString += c

    return resultString[::-1]

print(urlify2(str))
