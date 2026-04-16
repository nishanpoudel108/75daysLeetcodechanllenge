from collections import defaultdict
import bisect

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        # Step 1: map value -> indices
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = []
        
        for q in queries:
            value = nums[q]
            indices = pos[value]
            
            # If only one occurrence
            if len(indices) == 1:
                res.append(-1)
                continue
            
            # Binary search position
            i = bisect.bisect_left(indices, q)
            
            # Left neighbor (circular)
            left = indices[i - 1] if i > 0 else indices[-1]
            
            # Right neighbor (circular)
            right = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            # Compute circular distances
            dist_left = min(abs(q - left), n - abs(q - left))
            dist_right = min(abs(q - right), n - abs(q - right))
            
            res.append(min(dist_left, dist_right))
        
        return res