class Solution(object):
    def mirrorDistance(self, n):
        # Reverse the number
        rev = int(str(n)[::-1])
        
        # Return absolute difference
        return abs(n - rev)