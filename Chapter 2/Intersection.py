# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

# Class declaration for Node
class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None

# Helper functions
def create_list(nums):
    # for num in nums:
    if not nums:
        return None
    node = Node(nums[0])
    node.next = create_list(nums[1:])
    return node

def print_list(node):
    while node:
        print(node)
        node = node.next

#Sample method to intersect 2 linked lists for testing using arbitrary conditions
def intersect(root1,root2):
    while root1 and root2:
        if root1.next.val == root2.next.val:
            root2.next = root1.next
            return
        root1 = root1.next
        root2 = root2.next

# Method 1: Use a hashset

def intersection_set(root1, root2):
    visited = set()
    while root1:
        visited.add(root1)
        root1 = root1.next
    while root2:
        if root2 in visited:
            return True
        root2 = root2.next
    return False


def intersection_traverse(root1, root2):
    headA, headB = root1, root2
    while headA != headB:
        headA = root2 if headA is None else headA.next
        headB = root1 if headB is None else headB.next
    # print(headA.val, headB.val)
    return True if headA else False

nums1 = [1,2,3,4,5,6]
nums2 = [-1,-2,-3,4,5,6]
root1 = create_list(nums1)
root2  = create_list(nums2)

intersect(root1, root2)
print_list(root1)
print_list(root2)
# print(intersection_set(root1,root2))
print(intersection_traverse(root1,root2))