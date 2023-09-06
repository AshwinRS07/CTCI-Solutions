# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# Use two pointers with an index difference of k and then go till end for both. Slow pointer is the kth from last element


# Class declaration for Node
class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None


def kth_from_last(root, k):
    slow = fast = root
    if not root: return None
    while k > 1 and fast and fast.next:
        fast = fast.next
        k -= 1
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow.val







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

nums = [1,3,4,5,6,7,0]
root = create_list(nums)
print(kth_from_last(root, 1))