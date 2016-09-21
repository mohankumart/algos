#!/usr/bin/python
str = raw_input("Enter string: ")

# https://en.wikipedia.org/wiki/Plane_%28Unicode%29
# http://www.ascii-code.com/

def isUnique():
    test_dict = dict()
    is_unique = True
    for c in str:
        if(not test_dict.get(c, False)):
            test_dict[c] = c
        else:
            is_unique = False
            break
    if is_unique:
        return "String is unique"
    else:
        return "String is not unique"

print(isUnique())
