# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def first_common_ancestor(root,p,q):
    if not root:
        return None
    if root == p or root == q:
        return root
    left = first_common_ancestor(root.left)
    right = first_common_ancestor(root.right)
    if left and right:
        return root
    else:
        if left: return left
        if right: return right