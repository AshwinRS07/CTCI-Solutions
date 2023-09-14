# Validate BST: Implement a function to check if a binary tree is a binary search tree.

import math
def validate_bst(self, root) -> bool:
        def helper(node, low = float(-math.inf), high = float(math.inf)):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (helper(node.left, low, node.val) and helper(node.right, node.val, high))
        return helper(root)