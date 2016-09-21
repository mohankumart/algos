str1 = raw_input('Enter First String: ')
str2 = raw_input('Enter Second String: ')

def check_permutation(str1, str2):
    if(len(str1) != len(str2)):
        return 'Not Permutation strings'
    #initialize the track_duplicates to 0 to track if the exsisting character at the index of str2 is already matched
    #import pdb;pdb.set_trace()
    track_duplicates = [0] * len(str2) 
    is_permutations = True
    for c1 in str1:
        c1_in_str2 = False
        i = 0
        for c2 in str2:
            if(c1 == c2 and track_duplicates[i] is 0):
                c1_in_str2 = True
                track_duplicates[i] = 1
                break
            i += 1
        if(not c1_in_str2):
            is_permutations = False
            break
    if(is_permutations):
        return 'Permutation Strings'
    else:
        return 'Not Permutaions Strings'


print(check_permutation(str1, str2))
