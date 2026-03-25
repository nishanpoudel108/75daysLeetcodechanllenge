class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        total_sum = sum(sum(row) for row in grid)
        
        # If total sum is odd, cannot split equally
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # Check horizontal cuts
        current_sum = 0
        for i in range(m - 1):  # cut after row i
            current_sum += sum(grid[i])
            if current_sum == target:
                return True
        
        # Check vertical cuts
        current_sum = 0
        col_sums = [0] * n
        
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]
        
        for j in range(n - 1):  # cut after column j
            current_sum += col_sums[j]
            if current_sum == target:
                return True
        
        return False