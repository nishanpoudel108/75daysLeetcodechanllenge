"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        # original node -> cloned node
        clones = {}
        
        def dfs(curr):
            # If already cloned, return it
            if curr in clones:
                return clones[curr]
            
            # Create copy of current node
            copy = Node(curr.val)
            clones[curr] = copy
            
            # Clone neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)