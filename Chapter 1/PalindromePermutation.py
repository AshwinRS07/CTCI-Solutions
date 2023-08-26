# Given a string, write a function to check if it is a permutation of a palindrome.A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

#Idea: Use hashmap to count character (char -> count)occurences, we can have a maximum of 1 character with an odd count.

def palindrome_permutation(input_string: str) -> bool:
    odd_flag = False
    counter = {}
    for char in input_string:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    for key,value in counter.items():
        if value%2 == 0:
            continue
        elif not odd_flag:
            odd_flag = True
        else:
            return False
    return True


tests = ['abcdcab', 'qwerty','ashash']

for test in tests:
    print(palindrome_permutation(test))
    