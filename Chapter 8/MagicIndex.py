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

# Binary Search:
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

# Follow Up

def magic_index_follow_up_main(numbers):
    return magic_index_follow_up(numbers, 0 ,len(numbers)-1)

def magic_index_follow_up(numbers, l, r):
    if l > r: return -1
    mid = (l+r)//2
    if mid == numbers[mid]:
        return mid
    left_idx = min(mid-1, numbers[mid])
    left = magic_index_follow_up(numbers, l, left_idx)
    if left >=0: return left

    right_idx = max(mid+1, numbers[mid])
    right = magic_index_follow_up(numbers,r,right)
    return right

tests = [[-10,1,3,6,8,10,11]]
for test in tests:
    print(magic_index_bsearch(test))
    print(magic_index_follow_up_main(test))