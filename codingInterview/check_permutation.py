str1 = raw_input('Enter First String: ')
str2 = raw_input('Enter Second String: ')

def check_permutation(str1, str2):
    if(len(str1) != len(str2)):
        return 'Not Permutation strings'
    dup_list = list()
    is_permutations = True
    for c1 in str1:
        c1_in_str2 = False
        for c2 in str2:
            if(c1 == c2):
                c1_in_str2 = True
                break
        if(not c1_in_str2):
            is_permutations = False
            break
    if(is_permutations):
        return 'Permutation Strings'
    else:
        return 'Not Permutaions Strings'


print(check_permutation(str1, str2))
