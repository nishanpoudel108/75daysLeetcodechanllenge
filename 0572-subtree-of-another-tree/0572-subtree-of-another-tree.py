class Solution(object):
    
    def isSameTree(self, p, q):
        # Both null → same
        if not p and not q:
            return True
        
        # One null or values differ → not same
        if not p or not q or p.val != q.val:
            return False
        
        # Check left and right
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
    
    
    def isSubtree(self, root, subRoot):
        # If root is empty → can't contain subtree
        if not root:
            return False
        
        # Check current node OR left OR right
        if self.isSameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))