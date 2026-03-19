class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        
        count = 0
        
        # Prefix sums
        sumXY = [[0]*n for _ in range(m)]
        countX = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Convert values
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                x_val = 1 if grid[i][j] == 'X' else 0
                
                # Build prefix sums
                sumXY[i][j] = val
                countX[i][j] = x_val
                
                if i > 0:
                    sumXY[i][j] += sumXY[i-1][j]
                    countX[i][j] += countX[i-1][j]
                if j > 0:
                    sumXY[i][j] += sumXY[i][j-1]
                    countX[i][j] += countX[i][j-1]
                if i > 0 and j > 0:
                    sumXY[i][j] -= sumXY[i-1][j-1]
                    countX[i][j] -= countX[i-1][j-1]
                
                # Check conditions
                if sumXY[i][j] == 0 and countX[i][j] > 0:
                    count += 1
        
        return count