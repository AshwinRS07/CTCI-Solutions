# Permutations without Dups: Write a method to compute all permutations of a string of unique
# characters.

def permutations_without_dups(input_str):
    def helper(i):
        global cur_str
        if i >= len(input_str):
            res.append(cur_str)
        else:
            cur_str += input_str[i]
            helper(i+1)
            cur_str = cur_str[:-1]
            helper(i+1)
    res = []
    global cur_str
    cur_str = ''
    helper(0)
    return res


tests = ['abc']

for test in tests:
    print(permutations_without_dups(test))
