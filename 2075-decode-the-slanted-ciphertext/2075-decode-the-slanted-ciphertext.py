class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText
        
        n = len(encodedText)
        cols = n // rows
        
        # Step 1: build matrix
        matrix = []
        index = 0
        for i in range(rows):
            matrix.append(list(encodedText[index:index+cols]))
            index += cols
        
        # Step 2: read diagonally
        result = []
        
        for start_col in range(cols):
            i, j = 0, start_col
            
            while i < rows and j < cols:
                result.append(matrix[i][j])
                i += 1
                j += 1
        
        # Step 3: remove trailing spaces
        return "".join(result).rstrip()