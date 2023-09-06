# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.

# Instead of dealing with nodes, we change the value of each node to value of node.next and delete the last node.

def delete_middle_node(node):
    nxt = node.next
    while nxt:
        node.val = nxt.val
        node = node.next
        nxt = nxt.next
    # print(node.val)
    node.next = None

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

def get_node_from_value(val, root):
    while root and root.next:
        if root.val == val:
            return root
        root = root.next
    return None
nums = [1,2,3,4,5,6,7,8,9,0]
root = create_list(nums)
node = get_node_from_value(5, root)
delete_middle_node(node)
print_list(root)