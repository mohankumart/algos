#check palindrome
import re


def checkPalindrome(str):
    new_string = re.sub(r'\s|\.','',str)
    print(new_string) 
    stringlen = len(new_string)
    start = 0
    end = stringlen - 1
    mid = stringlen/2
    is_palindrome = True
    #import pdb;pdb.set_trace()
    for i in range(mid):
        #print(end)
        if new_string[start] != new_string[end]:
            is_palindrome = False
            break
        start += 1
        end -= 1 
    return is_palindrome

#palin_str = raw_input("Enter the string: ")
#if checkPalindrome(palin_str):
#    print("Yes it is palindrome")
#else:
#    print("No it is not palindrome")

def getCharValue(char):
    a = ord('a')
    z = ord('z')
    char_val = ord(char)
    if char_val >= a and char_val <= z:
        return char_val-a
    else:
        return -1 

def initializelist():
    my_list = list()
    for i in range(26):
        my_list.append(0)
    print my_list
    return my_list

def check_palindrome2(str):
    my_list = initializelist()
    oddCount = 0
    for c in str:
        c_value = getCharValue(c)
        #import pdb;pdb.set_trace()
        if c_value != -1:
            my_list[c_value] += 1
            if my_list[c_value]%2 == 1:
                oddCount += 1
            else:
                oddCount -= 1
    if oddCount <= 1:
        return 'It is palindrome'
    else:
        return 'It is not palindrome'

str = raw_input('Enter string: ')

print(check_palindrome2(str))
