# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if not node:
                return
            
            result.append(node.val)   # Visit root
            preorder(node.left)       # Traverse left
            preorder(node.right)      # Traverse right

        preorder(root)
        return result