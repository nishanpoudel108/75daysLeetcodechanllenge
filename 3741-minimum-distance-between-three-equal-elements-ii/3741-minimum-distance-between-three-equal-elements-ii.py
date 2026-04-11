class Solution(object):
    def minimumDistance(self, nums):
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        # Store indices for each number
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        # Process each number
        for indices in pos.values():
            if len(indices) >= 3:
                # Check consecutive triples
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i+2] - indices[i])
                    ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1