class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Build heights (histogram)
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        
        # Step 2: For each row
        for i in range(m):
            row = sorted(matrix[i], reverse=True)
            
            # Step 3: Calculate max area
            for j in range(n):
                height = row[j]
                width = j + 1
                max_area = max(max_area, height * width)
        
        return max_area