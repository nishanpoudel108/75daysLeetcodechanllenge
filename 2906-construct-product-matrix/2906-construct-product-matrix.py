class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        # Step 1: Flatten grid
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j] % MOD)
        
        size = len(arr)
        
        # Step 2: Prefix products
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
        # Step 3: Suffix products
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
        # Step 4: Build result
        result = [[0] * m for _ in range(n)]
        
        idx = 0
        for i in range(n):
            for j in range(m):
                result[i][j] = (prefix[idx] * suffix[idx]) % MOD
                idx += 1
        
        return result