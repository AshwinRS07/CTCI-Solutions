# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

def is_balanced(self, root) -> bool:
    def dfs(root):
        if not root:
            return [True,0]
        left,right = dfs(root.left),dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
        return [balanced,1 + max(left[1],right[1])]
    return dfs(root)[0]