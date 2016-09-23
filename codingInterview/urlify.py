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

print(urlify(str))
