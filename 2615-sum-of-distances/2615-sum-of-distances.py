class Solution(object):
    def distance(self, nums):
        from collections import defaultdict
        
        index_map = defaultdict(list)
        
        # Step 1: group indices
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        res = [0] * len(nums)
        
        # Step 2: process each group
        for positions in index_map.values():
            n = len(positions)
            
            # prefix sum
            prefix = [0] * (n + 1)
            for i in range(n):
                prefix[i + 1] = prefix[i] + positions[i]
            
            # Step 3: compute distances
            for i in range(n):
                left = i * positions[i] - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - (n - i - 1) * positions[i]
                res[positions[i]] = left + right
        
        return res