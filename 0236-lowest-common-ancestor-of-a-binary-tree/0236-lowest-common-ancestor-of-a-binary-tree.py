# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # Base case
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both sides return non-null,
        # current node is the LCA
        if left and right:
            return root
        
        # Otherwise return the non-null side
        return left if left else right