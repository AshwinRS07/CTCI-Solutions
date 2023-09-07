# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

from random import randrange;
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
    k = 10
    while k!= 0:
        print(node.val)
        node = node.next
        k -= 1

def create_cycle(root1, k):
    temp = k
    while k!= 0:
        root1 = root1.next
        k -= 1
    cycle = root1
    while root1.next:
        root1 = root1.next
    root1.next = cycle
    return temp

# Method 1: HashSet
def loop_detection_set(root):
    visited = set()
    while root:
        if root in visited:
            return root.val
        visited.add(root)
        root = root.next
    return

# Method 2: 2 pointers

def loop_detection_2ptr(root):
    slow = fast = root
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    fast = root
    while slow!=fast:
        slow,fast = slow.next,fast.next
    return slow.val

nums = [1,3,3,4,5]
root = create_list(nums)
create_cycle(root, randrange(0,len(nums)))
print_list(root)
# print("Answer:", loop_detection_set(root))
print("Answer:", loop_detection_2ptr(root))