class Solution(object):
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        res = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                
                vals = [grid[x][y] 
                        for x in range(i, i + k) 
                        for y in range(j, j + k)]
                
                vals.sort()
                
                min_diff = float('inf')
                
                for a, b in zip(vals, vals[1:]):
                    if a != b:  # only consider distinct values
                        min_diff = min(min_diff, b - a)
                
                row.append(min_diff if min_diff != float('inf') else 0)
            
            res.append(row)
        
        return res