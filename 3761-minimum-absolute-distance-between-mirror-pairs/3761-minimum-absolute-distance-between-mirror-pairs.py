class Solution(object):
    def minMirrorPairDistance(self, nums):
        def reverse_num(x):
            return int(str(x)[::-1])
        
        seen = {}
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            # If current number already expected
            if num in seen:
                min_dist = min(min_dist, i - seen[num])
            
            rev = reverse_num(num)
            seen[rev] = i   # store what we expect in future
        
        return min_dist if min_dist != float('inf') else -1