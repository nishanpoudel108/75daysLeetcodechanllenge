class Solution(object):
    def maxDistance(self, colors):
        n = len(colors)
        
        # Case 1: compare with first house
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                d1 = i
                break
        
        # Case 2: compare with last house
        for i in range(n):
            if colors[i] != colors[n - 1]:
                d2 = (n - 1) - i
                break
        
        return max(d1, d2)