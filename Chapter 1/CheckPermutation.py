# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other

# hash map

def check_permutation_hm(a,b):
    hashmap = {}
    for char in a:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1
    for char in b:
        if char not in hashmap or hashmap[char] == 0:
            return False
        else:
            hashmap[char] -= 1
    for key, value in hashmap.items():
        if value > 0:
            return False
    return True

string1 = "ash"
string2 = "hsah"

result = check_permutation_hm(string1,string2)
print(result)