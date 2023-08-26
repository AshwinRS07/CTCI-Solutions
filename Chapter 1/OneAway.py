# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(string1: str,string2: str) -> bool:
    if abs(len(string1)-len(string2)) > 1:
        return False
    equal_flag = len(string1) == len(string2)
    def helper(i,j,differences):
        if differences > 1:
            return False
        while i<len(string1) and j<len(string2):
            if string1[i] == string2[j]:
                print(i,j,differences,'equal')
                i += 1
                j += 1
            elif equal_flag:
                print(i,j,differences,'flag')
                return helper(i+1,j+1,differences+1)
            else:
                print(i,j,differences,'3calls')
                return helper(i+1,j,differences+1) or helper(i,j+1,differences+1) or helper(i+1,j+1,differences+1)
        while i<len(string1):
            differences += 1
            i += 1
        while j< len(string2):
            differences += 1
            j += 1
        if differences > 1:
            return False
        return True
    return helper(0,0,0)

tests = [['pale','pales'],['pale','bake'],['pale','ale']]

for string1, string2 in tests:
    print(one_away(string1,string2))