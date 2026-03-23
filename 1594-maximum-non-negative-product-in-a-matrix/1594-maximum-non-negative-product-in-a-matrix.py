class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp_max[i][j] = max product to reach (i,j)
        # dp_min[i][j] = min product to reach (i,j)
        dp_max = [[0]*n for _ in range(m)]
        dp_min = [[0]*n for _ in range(m)]
        
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        # First column
        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]
        
        # First row
        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]
        
        # Fill the DP table
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                
                candidates = [
                    dp_max[i-1][j] * val,
                    dp_min[i-1][j] * val,
                    dp_max[i][j-1] * val,
                    dp_min[i][j-1] * val
                ]
                
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        
        result = dp_max[m-1][n-1]
        
        if result < 0:
            return -1
        return result % MOD