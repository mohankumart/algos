#check if s2 is rotated string of s1

def check_rotation(s1, s2):
    str1Length = len(s1)
    str2Length = len(s2)
    if str1Length == str2Length:
        i = 0
        j = 0
        firstMatch = False
        #import pdb;pdb.set_trace()
        while i <= len(s1)-1:
            if s2[j] != s1[i]:
                if not firstMatch:
                    j += 1
                else:
                    return "String Failed"
            else:
                firstMatch = True 
                i += 1
                j += 1
            if j == len(s2):
                j = 0
        return "String Success"
    else:
        return "String Failed"

s1 = raw_input("Enter s1 string: ")
s2 = raw_input("Enter s2 string: ")

print(check_rotation(s1, s2))
