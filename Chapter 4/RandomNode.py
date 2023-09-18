# Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
import random
class tree_node:
    def __init__(self, val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find(root.left, val)
    right = find(root.right, val)
    if left: return left
    if right: return right

def random_node(root):
    node_val = random.choice(node_vals)
    find(node_val)

def insert():

def delete(val):
    node = find(val)
    