# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.


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


def partition(x, root):
    lstart = lesser = Node(0)
    gstart = greater = Node(0)

    while root:
        if root.val < x:
            lesser.next = root
            lesser = lesser.next
        else:
            greater.next = root
            greater = greater.next
        root = root.next
    new_head = lstart.next
    lesser.next = gstart.next
    return new_head

nums = [1,2,8,6,9,3,0,4,7]
root = create_list(nums)
# remove_dups(root)
head = partition(5, root)
print_list(head)