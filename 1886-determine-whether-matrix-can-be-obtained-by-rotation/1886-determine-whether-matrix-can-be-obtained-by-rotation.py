class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotate(matrix):
            # Transpose
            n = len(matrix)
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            # Reverse each row
            for row in matrix:
                row.reverse()
        
        # Try all 4 rotations
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False