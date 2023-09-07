# Palindrome: Implement a function to check if a linked list is a palindrome.

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
        print(node.val)
        node = node.next

def palindrome(root):
    slow = fast = root
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, slow, prev.next = slow, slow.next, None
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    fast, slow = root, prev
    while slow:
        if slow.val != fast.val:
            return False
        fast = fast.next
        slow = slow.next
    return True

nums = [1,3,3,3,1]
root = create_list(nums)
print(palindrome(root))
# print_list(root)