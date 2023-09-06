# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# Follow Up: Solve without any temporary buffer - Basically O(1) SC

# Base Solution: Using a hash set

# Class declaration for Node
class Node:
    def __init__(self, val:int):
        self.val = val
        self.next = None

def remove_dups(node):
    value_set = set()
    prev = node
    node = node.next if node.next else None
    while node and node.next:
        if node.val in value_set:
            prev.next = node.next
        else:
            value_set.add(node.val)
            prev = node
        node = node.next

# O(1) SC: Some bugs with this approach.

def remove_dups_no_set(node):
    current_node = node
    while current_node:
        prev = cur = current_node.next
        while cur and cur.next:
            if cur.val == current_node.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        current_node = current_node.next

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

nums = [1,3,3,4,5]
root = create_list(nums)
# remove_dups(root)
remove_dups_no_set(root)
print_list(root)