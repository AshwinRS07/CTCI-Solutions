# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Method 1: Create a Hash Set to keep a record of each occurence, if new char already exists in the set, there is repetition. Otherwise, just add the new unique char to the set.
# TC: O(n) SC: O(n)
def is_unique_set(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True

#Method 2: Sort the input string, and check pairs of consecutive characters for matching. If a match is found, no uniqueness. If string parses, Unique Chars.
#TC: O(nlogn) SC: O(1)
# def is_unique_sort(s):
#     s.sort()
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             return False
#     return True

input_string = "Ash"
print(is_unique_set(input_string))