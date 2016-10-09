#check palindrome

def checkPalindrome(str):
    stringlen = len(str)
    start = 0
    end = stringlen - 1
    mid = stringlen/2
    is_palindrome = True
    #import pdb;pdb.set_trace()
    for i in range(mid):
        print(end)
        if str[start] != str[end]:
            is_palindrome = False
            break
        start += 1
        end -= 1 
    return is_palindrome

palin_str = raw_input("Enter the string: ")
if checkPalindrome(palin_str):
    print("Yes it is palindrome")
else:
    print("No it is not palindrome")
