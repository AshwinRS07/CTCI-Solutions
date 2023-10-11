# Power Set: Write a method to return all subsets of a set.

def power_set(numbers):
    result_set = []
    subset = []

    def helper(i):
        if i >= len(numbers):
            result_set.append(subset[:])
        else:
            subset.append(numbers[i])
            helper(i+1)
            subset.pop()
            helper(i+1)
    helper(0)
    return result_set


tests = [[0,1,2], [-1,2,3,25]]

for test in tests:
    print(power_set(test))