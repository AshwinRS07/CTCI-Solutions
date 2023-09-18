# Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
def sameTree(self,s,t):
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right)
    return False