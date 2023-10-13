# Permutations with Duplicates: Write a method to compute all permutations of a string whose
# characters are not necessarily unique. The list of permutations should not have duplicates.

from collections import Counter

def permutations_with_duplicates(input_str):
    counts = Counter(input_str)
    # print(counts)
    def helper(counts, prefix, remaining, res):
        if remaining == 0:
            res.add(prefix)
        for key, count in counts.items():
            if count > 0:
                counts[key] -= 1
                helper(counts,prefix + key, remaining-1, res)
                counts[key] += 1
    res = set()
    helper(counts, '',len(input_str),res)
    return res


tests = ['abdd']
for test in tests:
    print(permutations_with_duplicates(test))