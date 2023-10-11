# Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
# i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.
# FOLLOW UP
# What if the values are not distinct?
# Hints:#770, #204, #240, #286, #340


# Naive
def magic_index_naive(numbers):
    for i, num in enumerate(numbers):
        if i == num:
            return i
    return -1

# Binary Search for Follow Up:
def magic_index_bsearch(numbers):
    l,r = 0, len(numbers)-1
    while l<r:
        mid = (l+r)//2
        if mid > numbers[mid]:
            l = mid
        elif mid < numbers[mid]:
            r = mid
        else:
            return mid


tests = [[0,2,3,6,8,10,11]]
for test in tests:
    print(magic_index_bsearch(test))