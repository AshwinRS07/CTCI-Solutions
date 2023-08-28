# Assume you have a method isSubstringwhich checks if one word is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

# Check each permutation for 1 string and if no match found, return false
def isSubstring(string1, string2)->bool:
    if len(string1)!=len(string2):
        return False
    if string1 == string2:
        return True
    for _ in range(len(string1)):
        string1 = string1[-1] + string1[:-1] 
        if string1 == string2:
            return True
    return False

tests = [['abcdef','efabcd'],['waterbottle','erbottlewat'],['turf','furt']]

for string1,string2 in tests:
    print(isSubstring(string1,string2))