class Solution(object):
    def minimumDistance(self, nums):
        from collections import defaultdict
        
        pos = defaultdict(list)
        
        # Store indices of each number
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        # Check each number's indices
        for indices in pos.values():
            if len(indices) >= 3:
                # Try all consecutive triples
                for i in range(len(indices) - 2):
                    i1 = indices[i]
                    i3 = indices[i + 2]
                    
                    distance = 2 * (i3 - i1)
                    ans = min(ans, distance)
        
        return ans if ans != float('inf') else -1