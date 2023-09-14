# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.


# Idea: Use binary search to create node from mid element, and recurse to create left and right children using bsearch as input

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

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

def minimal_tree(input_array):
    if len(input_array) < 1:
        return None
    else:
        mid = (len(input_array)-1)//2
        new_node = TreeNode(input_array[mid])
        new_node.left = minimal_tree(input_array[0:mid])
        new_node.right = minimal_tree(input_array[mid+1:])
    return new_node


input_array = [1,3,6,10,15,25]

root = minimal_tree(input_array)
print("Inorder:")
print_tree_inorder(root)
print("Preorder:")
print_tree_preorder(root)