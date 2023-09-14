# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

# Not working properly, revise later

from collections import deque

class Node:
    def __init__(self, val:int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def make_linked_list(nums):
    if len(nums) > 0:
        dummy = head = Node(nums[0])
        for i in range(1,len(nums)):
            node = Node(nums[i])
            head.next = node
            head = head.next
        return dummy

def list_of_depths(root):
    depths = []
    if root:
        depths.append(root)
    level = deque([[root]])
    while level:
        cur = level.popleft()
        new_level = []
        for node in cur:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        root = make_linked_list(new_level)
        level.append(new_level)
        depths.append(root)
    return depths

def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.val)
        print_tree_inorder(root.right)
    return

def print_tree_preorder(root):
    if root:
        print(root.val)
        print_tree_preorder(root.left)
        print_tree_preorder(root.right)
    return

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root = Node(preorder[0])
    midIndex = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:midIndex+1],inorder[:midIndex])
    root.right = build_tree(preorder[midIndex+1:],inorder[midIndex+1:])
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

root = build_tree(preorder,inorder)

depths = list_of_depths(root)

print(depths)