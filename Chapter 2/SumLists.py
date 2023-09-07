# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

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

def sum_lists(head1, head2):
    carry = 0
    resdummy = reshead = Node(0)
    while head1 and head2:
        addition = carry + head1.val + head2.val
        carry = addition//10
        resnode = Node(addition%10)
        # resnode.val = addition%10
        reshead.next = resnode
        reshead = reshead.next
        head1 = head1.next
        head2 = head2.next
    while head1:
        addition = carry + head1.val
        resnode = Node(addition%10)
        carry = addition//10
        haed1 = head1.next
        reshead.next = resnode
        reshead = reshead.next
    while head2:
        addition = carry + head2.val
        resnode = Node(addition%10)
        carry = addition//10
        haed2 = head2.next
        reshead.next = resnode
        reshead = reshead.next
    if carry:
        resnode = Node(carry)
        reshead.next = resnode
        # reshead = reshead.next
    return resdummy.next

nums1 = [1,2,3,4,5]
nums2 = [1,2,3,4,5]
root1 = create_list(nums1)
root2 = create_list(nums2)

head = sum_lists(root1,root2)
print_list(head)
