#oneway program

def oneaway(str1, str2):
    if len(str1) == len(str2): #one char replace from str2
        return oneCharReplaced(str1, str2)
    elif len(str1) + 1 == len(str2): #one extra char added in str2
        return oneCharDeleted(str1, str2)
    elif len(str1) - 1 == len(str2): #one char removed from str2
        return oneCharDeleted(str2, str1)

def oneCharReplaced(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

#str2 > str1 
def oneCharDeleted(str1, str2):
    index1 = 0
    index2 = 0
    while index1 <= len(str1)-1 and index2 <= len(str2)-1:
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True
str1 = raw_input('Enter str1: ')
str2 = raw_input('Enter str2: ')
print(oneaway(str1, str2))
