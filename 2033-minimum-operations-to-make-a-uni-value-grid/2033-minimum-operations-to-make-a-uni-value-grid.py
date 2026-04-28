class Solution(object):
    def minOperations(self, grid, x):
        arr = []
        
        # Flatten the grid
        for row in grid:
            for num in row:
                arr.append(num)
        
        # Check feasibility
        base = arr[0]
        for num in arr:
            if (num - base) % x != 0:
                return -1
        
        # Sort and find median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Calculate operations
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        
        return operations