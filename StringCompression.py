# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(input_str: str) -> str:
    original_length = len(input_str)
    new_str = ''
    i = 0
    while i<original_length:
        # prev = i
        j = i+1
        count = 1
        while j<original_length and i<original_length and input_str[j] == input_str[i]:
            count += 1
            j += 1
        new_str = new_str + input_str[i] + str(count)
        i = j
    return new_str if len(new_str) < original_length else input_str

tests = ['aabcccccaaa','aabbccdde','aaaaqqqqwe']

for test in tests:
    print(string_compression(test))