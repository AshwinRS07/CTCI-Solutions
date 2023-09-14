# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def succesor(root, node):
    succesor = None
    while root:
        if node.val >= root.val:
            root = root.right
        else:
            succesor = root
            root = root.left
    return succesor